from datetime import date
from typing import Any, Coroutine, Dict, Optional

from nsrdesafio01.src.api.nasa_api import NasaApodApi
from nsrdesafio01.src.api.telegram_bot_api import (
    TelegramBotApi,
    TelegramCommand,
)
from nsrdesafio01.src.dto.telegram_api_response_dto import TelegramApiResponse


class BotOrchestrator:
    def __init__(self, nasa_apod_gateway: NasaApodApi, telegram_bot_gateway: TelegramBotApi):
        """Initialize the BotOrchestrator.

        Args:
            nasa_apod_gateway (NasaApodApi): Instance of the NasaApodApi.
            telegram_bot_gateway (TelegramBotApi): Instance of the TelegramBotApi.
        """
        self._nasa_apod_gateway = nasa_apod_gateway
        self._telegram_bot_gateway = telegram_bot_gateway

    async def poll_and_send(self):
        """Polls for updates from Telegram and handles the received commands accordingly."""
        update = await self._telegram_bot_gateway.poll_telegram_updates()
        if not update:
            return

        await self.handle_command(update)

    def handle_mapper(self, command: str) -> Coroutine[None, None, None]:
        """Maps the command to the corresponding handler function.

        Args:
            command (str): The command to be mapped.

        Returns:
            Coroutine[None, None, None]: The corresponding handler function.
        """
        supported_funcs = {
            TelegramCommand.START.value: self._handle_start_command,
            TelegramCommand.GET_APOD.value: self._handle_nasa_apod,
            TelegramCommand.HELP.value: self._handle_help_command,
        }

        func = supported_funcs.get(command)
        return func

    async def _handle_nasa_apod(self, chat_id: int, date: Optional[date] = None) -> None:
        """Handles the GET_APOD command from the user.

        Args:
            chat_id (int): The ID of the chat where the command was received.
            date (Optional[date], optional): The specific date for which to get the APOD. Defaults to None.
        """
        apod_data = await self._nasa_apod_gateway.get_apod(date)

        if apod_data.media_type == "image":
            await self._send_nasa_apod_summary(chat_id)
            await self._telegram_bot_gateway.send_photo(chat_id, apod_data.url, apod_data.title)
            await self._telegram_bot_gateway.send_message(chat_id, apod_data.explanation)
        else:
            message = "Today's APOD is not an image. Check it out on the NASA APOD website!"
            await self._telegram_bot_gateway.send_message(chat_id, message)

    async def _send_nasa_apod_summary(self, chat_id: int) -> TelegramApiResponse:
        """
        Handles the /start command from the user.

        Args:
            chat_id (int): The chat ID from which the command was received.

        Returns:
            TelegramApiResponse: The response from the Telegram API.
        """
        response_text = (
            "In the next message, I'll send you the Astronomy Picture of the Day (APOD) image and its description. 🌌"
        )
        return await self._telegram_bot_gateway.send_message(chat_id, response_text)

    async def _handle_start_command(self, chat_id: int) -> TelegramApiResponse:
        """
        Handles the /start command from the user.

        Args:
            chat_id (int): The chat ID from which the command was received.

        Returns:
            TelegramApiResponse: The response from the Telegram API.
        """
        response_text = (
            "👋 Hello from NasaApoImages. How can I assist you today? 🚀\n\n"
            "Type /help for a list of available commands and how to use them. 💡"
        )
        return await self._telegram_bot_gateway.send_message(chat_id, response_text)

    async def _handle_help_command(self, chat_id: int) -> TelegramApiResponse:
        """
        Handles the /help command from the user.

        Args:
            chat_id (int): The chat ID from which the command was received.

        Returns:
            TelegramApiResponse: The response from the Telegram API.
        """
        response_text = (
            "🌟 Here are some available commands and how to use them:\n\n"
            "/getapod -> Get the astronomy picture of the day. 📷\n"
            "/getapodbydate -> Get the astronomy picture of a specific date. 🗓\n\n"
            "Feel free to explore! ✨"
        )
        return await self._telegram_bot_gateway.send_message(chat_id, response_text)

    async def _send_invalid_command_message(self, chat_id: int, invalid_message: str) -> TelegramApiResponse:
        """
        Sends a message about an invalid command to the specified chat ID.

        Args:
            chat_id (int): The chat ID to which the message should be sent.
            invalid_message (str): The invalid command received.

        Returns:
            TelegramApiResponse: The response from the Telegram API.
        """
        return await self._telegram_bot_gateway.send_message(
            chat_id, f"Invalid message: {invalid_message}. Please see the help menu for valid messages"
        )

    async def handle_command(self, updates: Dict[str, Any]) -> None:
        """Handle commands received from the user.

        Args:
            update (Dict[str, Any]): The update received from the user.

        Returns:
            None
        """
        # Extract the chat ID and message text from the update
        chat_id = self._telegram_bot_gateway.extract_chat_id_from_updates(updates)
        message_text = self._telegram_bot_gateway.extract_message_text_from_updates(updates)
        try:
            handler = self.handle_mapper(message_text)
            await handler(chat_id)
        except (TypeError, KeyError):
            await self._telegram_bot_gateway.send_invalid_command_message(chat_id, message_text)
