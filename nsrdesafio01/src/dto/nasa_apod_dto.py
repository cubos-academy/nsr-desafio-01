from __future__ import annotations

from typing import Dict

from pydantic import BaseModel, ValidationError


class NasaApoDto(BaseModel):
    """Data transfer object (DTO) representing data from the NASA Astronomy Picture of the Day (APOD) API."""

    url: str
    title: str
    explanation: str
    copyright: str
    media_type: str

    @classmethod
    def create(cls, apod_data: Dict[str, str]) -> NasaApoDto:
        """Creates a NasaApoDto object from a dictionary of APOD data.

        Args:
            apod_data (Dict[str, str]): The dictionary containing APOD data.

        Returns:
            NasaApoDto: The NasaApoDto object created from the provided data.

        Raises:
            ValueError: If any attribute is missing or the data is invalid.
        """
        required_attrs = ["url", "title", "explanation", "copyright", "media_type"]
        for attr in required_attrs:
            if attr not in apod_data:
                raise ValueError(f"Missing attribute: {attr}")
        try:
            return NasaApoDto.model_validate(apod_data)
        except ValidationError as e:
            raise ValueError(f"Invalid data: {e}")
