from datetime import UTC, datetime
from typing import Any

from app.schemas.property_record import PropertyRecord
from app.validators.duplicates import find_duplicate_records


def build_validation_report(records: list[PropertyRecord]) -> dict[str, Any]:
    duplicates = find_duplicate_records(records)

    return {
        "generated_at": datetime.now(UTC).isoformat(),
        "total_records": len(records),
        "valid_records": len(records),
        "duplicate_records": len(duplicates),
        "missing_street_address": count_missing_field(records, "street_address"),
        "missing_city": count_missing_field(records, "city"),
        "missing_county": count_missing_field(records, "county"),
        "missing_zip_code": count_missing_field(records, "zip_code"),
        "missing_notes": count_missing_field(records, "notes"),
    }


def count_missing_field(records: list[PropertyRecord], field_name: str) -> int:
    missing_count = 0

    for record in records:
        value = getattr(record, field_name)
        if value is None or value == "":
            missing_count += 1

    return missing_count
