from app.schemas.property_record import PropertyRecord
from app.validators.duplicates import build_duplicate_key, find_duplicate_records


def make_record(
    property_name: str = "Sample Park",
    street_address: str = "123 Main Street",
    city: str = "Orlando",
    state: str = "FL",
    source_url: str = "https://example.com/sample-park",
) -> PropertyRecord:
    return PropertyRecord(
        property_name=property_name,
        street_address=street_address,
        city=city,
        state=state,
        county="Orange County",
        source_name="Sample Directory",
        source_url=source_url,
    )


def test_build_duplicate_key_normalizes_text() -> None:
    record = make_record(
        property_name="  Sample   Park ",
        street_address=" 123   Main Street ",
        state="fl",
    )

    assert build_duplicate_key(record) == (
        "sample park",
        "123 main street",
        "fl",
    )


def test_find_duplicate_records_returns_repeated_records() -> None:
    records = [
        make_record(),
        make_record(source_url="https://example.com/sample-park-copy"),
        make_record(property_name="Different Park"),
    ]

    duplicates = find_duplicate_records(records)

    assert len(duplicates) == 1
    assert duplicates[0].source_url.unicode_string() == (
        "https://example.com/sample-park-copy"
    )


def test_find_duplicate_records_ignores_different_addresses() -> None:
    records = [
        make_record(street_address="123 Main Street"),
        make_record(street_address="456 Main Street"),
    ]

    duplicates = find_duplicate_records(records)

    assert duplicates == []
