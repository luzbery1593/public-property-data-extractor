from pathlib import Path
from typing import Any

import pandas as pd

from app.normalizers.text import normalize_optional_text, normalize_required_text
from app.schemas.property_record import PropertyRecord

FLORIDA_HEALTH_SOURCE_URL = (
    "https://www.floridahealth.gov/licensing-regulations/"
    "regulated-facilities/mobile-home-rv-parks/"
)


def import_florida_health_records(input_path: Path) -> list[PropertyRecord]:
    dataframe = pd.read_excel(input_path)
    records: list[PropertyRecord] = []

    for row in dataframe.to_dict(orient="records"):
        property_name = clean_cell(row.get("Company Name"))
        state = clean_cell(row.get("State"))

        if property_name is None or state is None:
            continue

        records.append(
            PropertyRecord(
                property_name=normalize_required_text(property_name),
                street_address=clean_cell(row.get("Street Address")),
                city=clean_cell(row.get("City")),
                state=normalize_required_text(state),
                county=format_county(clean_cell(row.get("CountyName"))),
                zip_code=format_zip_code(row.get("ZipCode")),
                source_name="Florida Department of Health",
                source_url=FLORIDA_HEALTH_SOURCE_URL,
                notes=build_notes(row),
            )
        )

    return records


def clean_cell(value: Any) -> str | None:
    if value is None or pd.isna(value):
        return None

    text = str(value).strip()
    return normalize_optional_text(text)


def format_zip_code(value: Any) -> str | None:
    if value is None or pd.isna(value):
        return None

    if isinstance(value, float):
        value = int(value)

    text = str(value).strip()

    if text.endswith(".0"):
        text = text[:-2]

    if text.isdigit() and len(text) < 5:
        text = text.zfill(5)

    return text or None


def format_county(value: str | None) -> str | None:
    if value is None:
        return None

    if value.casefold().endswith(" county"):
        return value

    return f"{value} County"


def build_notes(row: dict[str, Any]) -> str | None:
    note_parts = []

    permit_number = clean_cell(row.get("Permit Number"))
    program_subtype = clean_cell(row.get("Program SubType"))
    mobile_home_spaces = clean_cell(row.get("Number Of Mobile Home Spaces"))
    rv_spaces = clean_cell(row.get("Number Of Recreational Vehicle Spaces"))
    tent_spaces = clean_cell(row.get("Number Of Tent Spaces"))

    if permit_number:
        note_parts.append(f"Permit Number: {permit_number}")
    if program_subtype:
        note_parts.append(f"Program SubType: {program_subtype}")
    if mobile_home_spaces:
        note_parts.append(f"Mobile Home Spaces: {mobile_home_spaces}")
    if rv_spaces:
        note_parts.append(f"RV Spaces: {rv_spaces}")
    if tent_spaces:
        note_parts.append(f"Tent Spaces: {tent_spaces}")

    return "; ".join(note_parts) or None
