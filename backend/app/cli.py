from pathlib import Path

import typer

from app.exporters.property_exporter import (
    export_records_to_csv,
    export_records_to_excel,
)
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

    csv_path = export_records_to_csv(records, output_dir / "sample_records.csv")
    excel_path = export_records_to_excel(records, output_dir / "sample_records.xlsx")

    typer.echo(f"CSV exported to {csv_path}")
    typer.echo(f"Excel exported to {excel_path}")


def main() -> None:
    app()
