from app.normalizers.text import normalize_optional_text
from app.schemas.property_record import PropertyRecord


def build_duplicate_key(record: PropertyRecord) -> tuple[str, str, str]:
    property_name = normalize_optional_text(record.property_name) or ""
    street_address = normalize_optional_text(record.street_address) or ""

    return (
        property_name.casefold(),
        street_address.casefold(),
        record.state.casefold(),
    )


def find_duplicate_records(records: list[PropertyRecord]) -> list[PropertyRecord]:
    seen_keys: set[tuple[str, str, str]] = set()
    duplicates: list[PropertyRecord] = []

    for record in records:
        duplicate_key = build_duplicate_key(record)

        if duplicate_key in seen_keys:
            duplicates.append(record)
            continue

        seen_keys.add(duplicate_key)

    return duplicates
