import asyncio
import os

from dotenv import load_dotenv
from nsrdesafio01.src.api.nasa_api import NasaApodApi
from nsrdesafio01.src.api.telegram_bot_api import TelegramBotApi
from nsrdesafio01.src.bot_orchestrator import BotOrchestrator
from nsrdesafio01.src.gateways.http_gateway.async_http_gateway import (
    AsyncRequestsClient,
)


async def main_process():
    """Main entry point for the bot application."""

    load_dotenv()

    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    nasa_api_key = os.getenv("NASA_API_KEY")
    if not bot_token or not nasa_api_key:
        raise SystemExit("Missing TELEGRAM_BOT_TOKEN and NASA_API_KEY env variables")

    async_http_client = AsyncRequestsClient()
    nasa_apod_gateway = NasaApodApi(async_http_client, nasa_api_key)
    telegram_bot_gateway = TelegramBotApi(async_http_client, bot_token)
    orchestrator = BotOrchestrator(nasa_apod_gateway, telegram_bot_gateway)
    while True:
        await orchestrator.poll_and_send()
        await asyncio.sleep(1)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="NasaApoImages Bot Command Line Interface")
    parser.add_argument(
        "--run",
        action="store_true",
        help="Run the NasaApoImages bot",
    )

    args = parser.parse_args()

    if args.run:
        try:
            asyncio.run(main_process())
        except KeyboardInterrupt:
            raise SystemExit("System interrupted by the user")
    else:
        parser.print_help()
