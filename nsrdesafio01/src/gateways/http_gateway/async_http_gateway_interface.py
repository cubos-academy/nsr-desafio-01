from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class AsyncHTTPClient(ABC):
    """Asynchronous HTTP client interface."""

    header: Dict[str, str] = {"accept": "application/json", "Content-Type": "application/json"}

    @abstractmethod
    async def get(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        timeout: int = 10,
    ) -> Dict[str, Any]:
        """Performs a GET request.

        Args:
            url (str): The URL to request.
            headers (Dict[str, str], optional): The headers to send with the request. Defaults to None.
            params (Dict[str, Any], optional): The query parameters to send with the request. Defaults to None.
            timeout (int): timeout of the response in seconds

        Returns:
            Dict[str, Any]: The response body as a dictionary.
        """
        pass

    @abstractmethod
    async def post(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Union[Dict[str, Any], List[Dict[str, str]]]] = None,
    ) -> Dict[str, Any]:
        """Performs a POST request.

        Args:
            url (str): The URL to request.
            headers (Dict[str, str], optional): The headers to send with the request. Defaults to None.
            params (Dict[str, Any], optional): The request body as a dictionary. Defaults to None.

        Returns:
            Dict[str, Any]: The response body as a dictionary.
        """
        ...
