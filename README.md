# Public Property Data Extractor

A backend data pipeline for converting public property directory pages into clean, validated CSV and Excel deliverables.

## Overview

Public Property Data Extractor demonstrates a structured approach to public data extraction work. It focuses on repeatable parsing, source traceability, schema validation, text normalization, duplicate detection, and reliable exports.

The MVP uses a local HTML fixture instead of live websites. This keeps the project testable, stable, and aligned with responsible source usage while still demonstrating the complete backend workflow.

## Features

- Command-line interface for validation and export workflows
- HTML directory parsing with BeautifulSoup
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
- Pytest
- Ruff

## Project Structure

```text
backend/
  app/
    extractors/
    normalizers/
    exporters/
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

## Data Fields

The MVP record schema includes:

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

## Methodology

See `docs/methodology.md` for collection rules, data quality rules, and current limitations.

See `docs/portfolio-notes.md` for project positioning and future improvement ideas.

## Current Limitations

- The current extractor uses a local HTML fixture for repeatable tests.
- Live source collection is not included in this MVP.
- New source extractors should be added only after reviewing source access rules and page structure.

## Future Improvements

- Add source-specific extractors for approved public sources.
- Add CSV input validation.
- Add richer duplicate review reports.
- Add optional SQLite storage.
- Add Docker support.
