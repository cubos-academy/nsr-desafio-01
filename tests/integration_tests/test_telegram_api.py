import pytest
from nsrdesafio01.src.api.telegram_bot_api import TelegramBotApi
from nsrdesafio01.src.dto.telegam_bot_commands_dto import BotCommand
from nsrdesafio01.src.gateways.http_gateway.async_http_gateway import (
    AsyncRequestsClient,
)


@pytest.fixture
def telegram_bot_token() -> str:
    import os

    from dotenv import load_dotenv

    load_dotenv()  # Load environment variables from .env file

    return os.getenv("TELEGRAM_BOT_TOKEN")


@pytest.mark.asyncio
async def est_set_command(telegram_bot_token: str):
    """Test to verify the behavior of the 'get_apod' method in the NasaApodApi class.

    This test checks whether the 'get_apod' method returns the expected keys in the response.
    """
    commands = [
        BotCommand(command="/start", description="Start the bot"),
        BotCommand(command="/getapod", description="Get the Astronomy Picture of the Day"),
        # Add more commands as needed
    ]
    # Arrange
    http_client = AsyncRequestsClient()
    telegram_api = TelegramBotApi(http_client, bot_token=telegram_bot_token)

    # Act
    result = await telegram_api.set_commands(commands)

    assert result.ok == True
    assert result.result == True
