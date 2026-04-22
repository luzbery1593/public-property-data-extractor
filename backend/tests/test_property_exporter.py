from pathlib import Path

import pandas as pd

from app.exporters.property_exporter import (
    EXPORT_COLUMNS,
    export_records_to_csv,
    export_records_to_excel,
    records_to_dataframe,
)
from app.schemas.property_record import PropertyRecord


def make_record() -> PropertyRecord:
    return PropertyRecord(
        property_name="Sample Park",
        street_address="123 Main Street",
        city="Orlando",
        state="FL",
        county="Orange County",
        zip_code="32801",
        source_name="Sample Directory",
        source_url="https://example.com/sample-park",
    )


def test_records_to_dataframe_uses_export_columns() -> None:
    dataframe = records_to_dataframe([make_record()])

    assert list(dataframe.columns) == EXPORT_COLUMNS
    assert dataframe.loc[0, "property_name"] == "Sample Park"


def test_export_records_to_csv_creates_file(tmp_path: Path) -> None:
    output_path = tmp_path / "records.csv"

    result_path = export_records_to_csv([make_record()], output_path)

    assert result_path == output_path
    exported = pd.read_csv(output_path)
    assert exported.loc[0, "property_name"] == "Sample Park"


def test_export_records_to_excel_creates_file(tmp_path: Path) -> None:
    output_path = tmp_path / "records.xlsx"

    result_path = export_records_to_excel([make_record()], output_path)

    assert result_path == output_path
    exported = pd.read_excel(output_path)
    assert exported.loc[0, "property_name"] == "Sample Park"
