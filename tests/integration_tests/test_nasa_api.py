import pytest
from nsrdesafio01.src.api.nasa_api import NasaApodApi
from nsrdesafio01.src.dto.nasa_apod_dto import NasaApoDto
from nsrdesafio01.src.gateways.http_gateway.async_http_gateway import (
    AsyncRequestsClient,
)


@pytest.fixture
def nasa_api_key() -> str:
    import os

    from dotenv import load_dotenv

    load_dotenv()  # Load environment variables from .env file

    return os.getenv("NASA_API_KEY")


@pytest.mark.asyncio
async def test_get_apod_endpoint(nasa_api_key: str):
    """Test to verify the behavior of the 'get_apod' method in the NasaApodApi class.

    This test checks whether the 'get_apod' method returns the expected keys in the response.
    """

    # Arrange
    http_client = AsyncRequestsClient()
    nasa_apod_api = NasaApodApi(http_client, api_key=nasa_api_key)

    # Act
    result = await nasa_apod_api.get_apod()

    # Assert
    assert isinstance(result, NasaApoDto)
