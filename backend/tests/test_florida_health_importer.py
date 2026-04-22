from pathlib import Path

import pandas as pd

from app.importers.florida_health import (
    format_county,
    format_zip_code,
    import_florida_health_records,
)


def test_format_zip_code_removes_excel_decimal() -> None:
    assert format_zip_code(32608.0) == "32608"


def test_format_zip_code_pads_short_zip_code() -> None:
    assert format_zip_code(1234.0) == "01234"


def test_format_county_appends_county_suffix() -> None:
    assert format_county("Orange") == "Orange County"


def test_import_florida_health_records_maps_rows(tmp_path: Path) -> None:
    input_path = tmp_path / "florida_health_sample.xlsx"
    dataframe = pd.DataFrame(
        [
            {
                "Permit Number": "01-54-00002",
                "CountyName": "Alachua",
                "Company Name": "The Palms of Archer",
                "Street Address": "7117 SW Archer Road",
                "City": "Gainesville",
                "State": "FL",
                "ZipCode": 32608.0,
                "Program SubType": "Mobile Home Park",
                "Number Of Mobile Home Spaces": 441.0,
                "Number Of Recreational Vehicle Spaces": 0.0,
                "Number Of Tent Spaces": 0.0,
            }
        ]
    )
    dataframe.to_excel(input_path, index=False)

    records = import_florida_health_records(input_path)

    assert len(records) == 1
    assert records[0].property_name == "The Palms of Archer"
    assert records[0].street_address == "7117 SW Archer Road"
    assert records[0].city == "Gainesville"
    assert records[0].state == "FL"
    assert records[0].county == "Alachua County"
    assert records[0].zip_code == "32608"
    assert "Permit Number: 01-54-00002" in (records[0].notes or "")
