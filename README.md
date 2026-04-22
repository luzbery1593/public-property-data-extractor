# Public Property Data Extractor

A backend data pipeline for converting public property directory and facility datasets into clean, validated CSV and Excel deliverables.

## Overview

Public Property Data Extractor demonstrates a structured approach to public data extraction work. It focuses on source traceability, schema validation, text normalization, duplicate detection, and reliable exports.

The project started with a local HTML fixture for repeatable parsing tests and now includes an importer for an official Florida Department of Health mobile home and RV park listing.

## Features

- Command-line interface for validation and export workflows
- HTML directory parsing with BeautifulSoup
- Official Excel dataset import workflow
- Typed property records with Pydantic validation
- Text normalization helpers
- Duplicate record detection
- CSV and Excel exports
- Automated tests with Pytest
- Linting and formatting with Ruff
- Documented methodology for responsible source handling

## Tech Stack

- Python
- Typer
- Pydantic
- BeautifulSoup
- Pandas
- OpenPyXL
- xlrd
- Pytest
- Ruff

## Project Structure

```text
backend/
  app/
    exporters/
    extractors/
    importers/
    normalizers/
    schemas/
    validators/
  tests/
docs/
exports/
```

## Setup

From the project root:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

## Run Tests

From `backend/` with the virtual environment active:

```bash
pytest
```

## Run Quality Checks

From `backend/` with the virtual environment active:

```bash
ruff check .
ruff format .
```

## Validate Sample Directory Data

From `backend/` with the virtual environment active:

```bash
property-extractor validate-sample-directory
```

Expected output:

```text
Valid records: 2
Duplicate records: 0
```

## Export Sample Directory Data

From `backend/` with the virtual environment active:

```bash
property-extractor export-sample-directory
```

This creates:

```text
../exports/sample_directory_records.csv
../exports/sample_directory_records.xlsx
```

## Import Florida Health Mobile Home and RV Park Data

Download the official Excel file from the Florida Department of Health mobile home and RV parks page:

```bash
mkdir -p data/raw
curl -L "https://www.floridahealth.gov/wp-content/uploads/2026/02/Current-MHP-List-1.26.2026.xls" -o data/raw/florida_mobile_home_rv_parks.xls
```

Then run the importer from `backend/` with the virtual environment active:

```bash
property-extractor import-florida-health --input ../data/raw/florida_mobile_home_rv_parks.xls
```

Example output:

```text
Records imported: 5202
Duplicate records: 1
Records exported: 5202
CSV exported to ../exports/florida_health_records.csv
Excel exported to ../exports/florida_health_records.xlsx
```

## Data Fields

The normalized MVP record schema includes:

- property_name
- street_address
- city
- state
- county
- zip_code
- source_name
- source_url
- collected_at
- notes

## Official Source

The Florida Health importer uses the official Florida Department of Health mobile home and RV parks listing published from:

```text
https://www.floridahealth.gov/licensing-regulations/regulated-facilities/mobile-home-rv-parks/
```

## Methodology

See `docs/methodology.md` for collection rules, data quality rules, and current limitations.

See `docs/portfolio-notes.md` for project positioning and future improvement ideas.

## Current Limitations

- The HTML extractor uses a local fixture for repeatable tests.
- The Florida Health importer depends on the structure of the official Excel file.
- New source importers should be added only after reviewing source access rules and data structure.

## Future Improvements

- Add validation report exports.
- Add duplicate review exports.
- Add CSV input validation.
- Add optional SQLite storage.
- Add Docker support for reproducible runs.
