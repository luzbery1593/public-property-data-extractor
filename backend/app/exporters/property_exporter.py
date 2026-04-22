from pathlib import Path

import pandas as pd

from app.schemas.property_record import PropertyRecord


EXPORT_COLUMNS = [
    "property_name",
    "street_address",
    "city",
    "state",
    "county",
    "zip_code",
    "source_name",
    "source_url",
    "collected_at",
    "notes",
]


def records_to_dataframe(records: list[PropertyRecord]) -> pd.DataFrame:
    rows = [
        record.model_dump(mode="json")
        for record in records
    ]

    return pd.DataFrame(rows, columns=EXPORT_COLUMNS)


def export_records_to_csv(records: list[PropertyRecord], output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe = records_to_dataframe(records)
    dataframe.to_csv(output_path, index=False)
    return output_path


def export_records_to_excel(records: list[PropertyRecord], output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe = records_to_dataframe(records)
    dataframe.to_excel(output_path, index=False)
    return output_path
