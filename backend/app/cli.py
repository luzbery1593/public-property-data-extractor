from pathlib import Path

import typer

from app.exporters.property_exporter import (
    export_records_to_csv,
    export_records_to_excel,
)
from app.extractors.sample_directory import extract_sample_directory
from app.schemas.property_record import PropertyRecord

app = typer.Typer(
    help="Collect and export public property directory data.",
    no_args_is_help=True,
)


@app.callback()
def cli() -> None:
    pass


def build_sample_record() -> PropertyRecord:
    return PropertyRecord(
        property_name="Sample Mobile Home Park",
        street_address="123 Main Street",
        city="Orlando",
        state="FL",
        county="Orange County",
        zip_code="32801",
        source_name="Sample Public Directory",
        source_url="https://example.com/sample-mobile-home-park",
        notes="Sample record for export verification.",
    )


@app.command()
def export_sample(
    output_dir: Path = typer.Option(
        Path("../exports"),
        "--output-dir",
        "-o",
        help="Directory where sample export files will be written.",
    ),
) -> None:
    records = [build_sample_record()]
    export_records(records, output_dir, "sample_records")


@app.command()
def export_sample_directory(
    input_path: Path = typer.Option(
        Path("tests/fixtures/sample_directory.html"),
        "--input",
        "-i",
        help="HTML file to parse.",
    ),
    output_dir: Path = typer.Option(
        Path("../exports"),
        "--output-dir",
        "-o",
        help="Directory where export files will be written.",
    ),
    base_url: str = typer.Option(
        "https://example.com",
        "--base-url",
        help="Base URL used to resolve relative source links.",
    ),
) -> None:
    records = extract_sample_directory(
        html_path=input_path,
        base_url=base_url,
    )
    export_records(records, output_dir, "sample_directory_records")


def export_records(records: list[PropertyRecord], output_dir: Path, file_stem: str) -> None:
    csv_path = export_records_to_csv(records, output_dir / f"{file_stem}.csv")
    excel_path = export_records_to_excel(records, output_dir / f"{file_stem}.xlsx")

    typer.echo(f"Records exported: {len(records)}")
    typer.echo(f"CSV exported to {csv_path}")
    typer.echo(f"Excel exported to {excel_path}")


def main() -> None:
    app()
