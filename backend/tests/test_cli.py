from pathlib import Path

import pandas as pd
from typer.testing import CliRunner

from app.cli import app

runner = CliRunner()


def test_export_sample_creates_csv_and_excel(tmp_path: Path) -> None:
    result = runner.invoke(
        app,
        ["export-sample", "--output-dir", str(tmp_path)],
    )

    assert result.exit_code == 0
    assert (tmp_path / "sample_records.csv").exists()
    assert (tmp_path / "sample_records.xlsx").exists()
    assert "Records exported: 1" in result.stdout


def test_export_sample_directory_creates_csv_and_excel(tmp_path: Path) -> None:
    result = runner.invoke(
        app,
        [
            "export-sample-directory",
            "--input",
            "tests/fixtures/sample_directory.html",
            "--output-dir",
            str(tmp_path),
        ],
    )

    assert result.exit_code == 0
    assert (tmp_path / "sample_directory_records.csv").exists()
    assert (tmp_path / "sample_directory_records.xlsx").exists()
    assert "Records exported: 2" in result.stdout


def test_validate_sample_directory_reports_valid_and_duplicate_records() -> None:
    result = runner.invoke(
        app,
        [
            "validate-sample-directory",
            "--input",
            "tests/fixtures/sample_directory.html",
        ],
    )

    assert result.exit_code == 0
    assert "Valid records: 2" in result.stdout
    assert "Duplicate records: 0" in result.stdout


def test_import_florida_health_creates_csv_and_excel(tmp_path: Path) -> None:
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

    result = runner.invoke(
        app,
        [
            "import-florida-health",
            "--input",
            str(input_path),
            "--output-dir",
            str(tmp_path),
        ],
    )

    assert result.exit_code == 0
    assert (tmp_path / "florida_health_records.csv").exists()
    assert (tmp_path / "florida_health_records.xlsx").exists()
    assert "Records imported: 1" in result.stdout
    assert "Duplicate records: 0" in result.stdout
