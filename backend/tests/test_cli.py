from pathlib import Path

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
