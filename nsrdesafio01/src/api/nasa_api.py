from datetime import date
from typing import Dict, Optional

from nsrdesafio01.src.dto.nasa_apod_dto import NasaApoDto
from nsrdesafio01.src.gateways.http_gateway.async_http_gateway_interface import (
    AsyncHTTPClient,
)


class NasaApodApi:
    """Class for interacting with the NASA APOD API."""

    _base_url = "https://api.nasa.gov/planetary/apod"

    def __init__(self, http_gateway: AsyncHTTPClient, api_key: str) -> None:
        """Initialize the NasaApodApi.

        Args:
            http_gateway (AsyncHTTPClient): The HTTP client for making API requests.
            api_key (str): The API key for authenticating the requests.
        """
        self._api_key = api_key
        self._http_gateway = http_gateway

    @staticmethod
    def _mount_api_key_query(api_key: str) -> Dict[str, str]:
        """Mounts the API key query.

        Args:
            api_key (str): The API key for the query.

        Returns:
            Dict[str, str]: The dictionary containing the API key.
        """
        return {"api_key": api_key}

    @property
    def base_url(self) -> str:
        """Get the base URL.

        Returns:
            str: The base URL.
        """
        return self._base_url

    @base_url.setter
    def base_url(self, url: str) -> None:
        """Set the base URL.

        Args:
            url (str): The new base URL.

        Raises:
            AttributeError: If the URL is invalid.
        """
        if not url.startswith("https://"):
            raise AttributeError(f"Invalid URL {url}")

        self._base_url = url

    async def get_apod(self, date: Optional[date] = None) -> NasaApoDto:
        """Fetch the Astronomy Picture of the Day based on the provided date.

        Args:
            date (datetime): The date for which to fetch the APOD.

        Returns:
            Response: The response from the APOD API.
        """
        query = self._mount_api_key_query(self._api_key)
        if date:
            query.update({"date": date.strftime("%Y-%m-%d")})

        apod_data = await self._http_gateway.get(self.base_url, params=query)
        return NasaApoDto.create(apod_data)
