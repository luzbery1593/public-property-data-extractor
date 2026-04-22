import pytest
from pydantic import ValidationError

from app.schemas.property_record import PropertyRecord


def test_property_record_normalizes_state() -> None:
    record = PropertyRecord(
        property_name="Sample Park",
        city="Orlando",
        state="fl",
        county="Orange County",
        source_name="Sample Directory",
        source_url="https://example.com/sample-park",
    )

    assert record.state == "FL"


def test_property_record_requires_property_name() -> None:
    with pytest.raises(ValidationError):
        PropertyRecord(
            property_name="",
            city="Orlando",
            state="FL",
            source_name="Sample Directory",
            source_url="https://example.com/sample-park",
        )


def test_property_record_rejects_invalid_zip_code() -> None:
    with pytest.raises(ValidationError):
        PropertyRecord(
            property_name="Sample Park",
            city="Orlando",
            state="FL",
            zip_code="ABC",
            source_name="Sample Directory",
            source_url="https://example.com/sample-park",
        )


def test_property_record_requires_address_or_city() -> None:
    with pytest.raises(ValidationError):
        PropertyRecord(
            property_name="Sample Park",
            state="FL",
            source_name="Sample Directory",
            source_url="https://example.com/sample-park",
        )
