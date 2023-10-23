import asyncio
from typing import Any, Dict, List, Optional, Union

import requests

from .async_http_gateway_interface import AsyncHTTPClient


class AsyncRequestsClient(AsyncHTTPClient):
    """Asynchronous HTTP client based on requests library."""

    async def get(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        timeout: int = 10,
    ) -> Dict[str, Any]:
        """Performs a GET request asynchronously.

        Args:
            url (str): The URL to request.
            headers (Dict[str, str], optional): The headers to send with the request. Defaults to None.
            params (Dict[str, Any], optional): The query parameters to send with the request. Defaults to None.
            timeout (int): timeout of the response in seconds

        Returns:
            Dict[str, Any]: The response body as a dictionary.

        Raises:
            requests.HTTPError: If the response status code is not within the range of 200-299.
        """
        loop = asyncio.get_event_loop()
        try:
            response = await loop.run_in_executor(None, requests.get, url, params)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as error:
            raise error

    async def post(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Union[Dict[str, Any], List[Dict[str, str]]]] = None,
    ) -> Dict[str, Any]:
        """Performs a POST request asynchronously.

        Args:
            url (str): The URL to request.
            headers (Dict[str, str], optional): The headers to send with the request. Defaults to None.
            params (Dict[str, Any], optional): The request body as a dictionary. Defaults to None.

        Returns:
            Dict[str, Any]: The response body as a dictionary.

        Raises:
            HTTPError: If the response status code is not within the range of 200-299.
        """
        loop = asyncio.get_event_loop()
        try:
            response = await loop.run_in_executor(None, requests.post, url, params)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as error:
            raise error
