from typing import Any, Dict, Union

from pydantic import BaseModel


class TelegramApiResponse(BaseModel):
    """Represents a response from the API.

    Attributes:
        ok (bool): Whether the request was successful or not.
        result (bool): The result from the API call.
    """

    ok: bool
    result: Union[bool, Dict[str, Any]]
