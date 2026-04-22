from datetime import UTC, datetime
from typing import Self

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    field_validator,
    model_validator,
)


class PropertyRecord(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    property_name: str = Field(min_length=1)
    street_address: str | None = None
    city: str | None = None
    state: str = Field(min_length=2, max_length=2)
    county: str | None = None
    zip_code: str | None = None
    source_name: str = Field(min_length=1)
    source_url: HttpUrl
    collected_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    notes: str | None = None

    @field_validator("state")
    @classmethod
    def normalize_state(cls, value: str) -> str:
        return value.upper()

    @field_validator("zip_code")
    @classmethod
    def validate_zip_code(cls, value: str | None) -> str | None:
        if value is None or value == "":
            return None

        digits = value.replace("-", "")
        if not digits.isdigit() or len(digits) not in {5, 9}:
            raise ValueError("zip_code must contain 5 or 9 digits")

        return value

    @model_validator(mode="after")
    def require_location_detail(self) -> Self:
        if not self.street_address and not self.city:
            raise ValueError("street_address or city is required")

        return self
