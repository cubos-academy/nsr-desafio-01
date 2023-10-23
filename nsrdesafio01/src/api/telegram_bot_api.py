import asyncio
import time
from collections import deque
from enum import Enum
from typing import Any, Deque, Dict, List, Optional

from nsrdesafio01.src.dto.telegam_bot_commands_dto import BotCommand
from nsrdesafio01.src.dto.telegram_api_response_dto import TelegramApiResponse
from nsrdesafio01.src.gateways.http_gateway.async_http_gateway_interface import (
    AsyncHTTPClient,
)


class TelegramCommand(Enum):
    """Enumeration for supported Telegram commands"""

    START = "/start"
    GET_APOD = "/getapod"
    HELP = "/help"


SUPPORTED_TELEGRAM_COMMANDS = [
    BotCommand(command=TelegramCommand.START.value, description="Start the bot"),
    BotCommand(command=TelegramCommand.GET_APOD.value, description="Get the Astronomy Picture of the Day"),
    BotCommand(command=TelegramCommand.HELP.value, description="See the help menu"),
]


class TelegramBotApi:
    _base_url = "https://api.telegram.org/bot"

    def __init__(self, http_gateway: AsyncHTTPClient, bot_token: str, max_processed_messages: int = 100) -> None:
        """Initialize the TelegramBotApi.

        Args:
            http_gateway (AsyncHTTPClient): The HTTP client for making API requests.
            bot_token (str): The token for accessing the Telegram Bot API.
        """
        self._bot_token = bot_token
        self._http_gateway = http_gateway
        self._max_processed_messages = max_processed_messages
        self._processed_message_ids: Deque[int] = deque(maxlen=max_processed_messages)

    async def send_message(self, chat_id: int, message: str) -> TelegramApiResponse:
        """Sends a message to the specified chat ID.

        Args:
            chat_id (int): The chat ID to which the message should be sent.
            message (str): The message to send.

        Returns:
            TelegramApiResponse: The response from the Telegram API.
        """
        endpoint = "/sendMessage"
        url = f"{self._base_url}{self._bot_token}{endpoint}"
        response = await self._http_gateway.post(url, params={"chat_id": chat_id, "text": message})
        return TelegramApiResponse(**response)

    async def get_updates(self, offset: Optional[int] = None) -> Dict[str, Any]:
        """Get updates from the Telegram Bot API.

        Returns:
            Dict[str, Any]: The response from the getUpdates endpoint.
        """
        method = "/getUpdates"
        url = f"{self._base_url}{self._bot_token}{method}"
        return await self._http_gateway.get(url, params={"offset": offset} if offset else None)

    async def send_photo(self, chat_id: int, photo_url: str, caption: str) -> TelegramApiResponse:
        """Sends a photo to the specified chat ID.

        Args:
            chat_id (int): The chat ID to which the photo should be sent.
            photo_url (str): The URL of the photo to be sent.
            caption (str): The caption for the photo.

        Returns:
            TelegramApiResponse: The response from the Telegram API.
        """
        method = "/sendPhoto"
        url = f"{self._base_url}{self._bot_token}{method}"
        payload = {"chat_id": chat_id, "photo": photo_url, "caption": caption}
        response = await self._http_gateway.post(url, params=payload)
        return TelegramApiResponse(**response)

    async def set_commands(self, commands: List[BotCommand]) -> TelegramApiResponse:
        """Sets the commands for the bot.

        Args:
            commands (List[BotCommand]): List of commands to be set for the bot.

        Returns:
            TelegramApiResponse: Response from the Telegram API.
        """
        endpoint = "/setMyCommands"
        url = f"{self._base_url}{self._bot_token}{endpoint}"

        response = await self._http_gateway.post(url, params=[command.model_dump() for command in commands])

        return TelegramApiResponse(**response)

    async def get_opened_chats(self) -> List[int]:
        """Retrieve all chat IDs for the Telegram bot.

        Returns:
            List[int]: List of all chat IDs.

        Raises:
            AttributeError: If no chats are found for the given Telegram bot.
        """
        updates = await self.get_updates()
        chat_ids = self.__get_all_chat_ids(updates)
        if not chat_ids:
            raise AttributeError("No chats found for the given Telegram bot")

        return chat_ids

    def extract_chat_id_from_updates(self, updates: Dict[str, Any]):
        """Extracts the chat ID from the received updates.

        Args:
            updates (Dict[str, Any]): The updates received from Telegram.

        Returns:
            int: The extracted chat ID.
        """
        return updates["message"]["chat"]["id"]

    def extract_message_text_from_updates(self, updates: Dict[str, Any]):
        """Extracts the message text from the received updates.

        Args:
            updates (Dict[str, Any]): The updates received from Telegram.

        Returns:
            str: The extracted message text.
        """
        return updates["message"]["text"]

    async def poll_telegram_updates(self):
        """Poll for updates from Telegram.

        This function polls for updates from Telegram and processes the latest message.
        """

        last_update = time.time() - 1  # Fetch updates from the last second
        updates = await self.get_updates(int(last_update))  # Method to get updates from Telegram
        results = updates.get("result", [])
        if not results:
            await asyncio.sleep(1)  # Sleep if there are no results
            return
        latest_update = results[-1]  # Get the latest message
        if "message" not in latest_update:
            await asyncio.sleep(1)  # Sleep if the latest update doesn't contain a message
            return
        latest_message_id = latest_update["message"]["message_id"]
        if latest_message_id in self._processed_message_ids:
            await asyncio.sleep(1)  # Sleep if the message has already been processed
            return
        self._processed_message_ids.append(latest_message_id)  # Add the message ID to the deque
        return latest_update

    def __get_all_chat_ids(self, data: Dict[str, Any]) -> List[int]:
        """Extract all chat IDs from the Telegram API response.

        Args:
            data (Dict[str, Any]): The Telegram API response data.

        Returns:
            List[int]: List of all chat IDs extracted from the data.
        """
        chat_ids: List[int] = []
        for result in data["result"]:
            chat_id = result["message"]["chat"]["id"]
            if chat_id not in chat_ids:
                chat_ids.append(chat_id)

        return chat_ids

    async def run_telegram_bot_forever(self):
        """Runs the Telegram bot continuously until stopped by the user."""
        await self.poll_telegram_updates()
