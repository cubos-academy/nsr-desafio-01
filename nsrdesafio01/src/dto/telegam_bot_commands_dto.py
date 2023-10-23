from pydantic import BaseModel


class BotCommand(BaseModel):
    """Represents a command for the Telegram bot.

    Attributes:
        command (str): The command keyword.
        description (str): Description of the command.
    """

    command: str
    description: str
