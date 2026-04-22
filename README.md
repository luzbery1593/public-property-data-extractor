# Public Property Data Extractor

Backend-only MVP for collecting, normalizing, validating, and exporting public property directory data from approved sources.

## Overview

This project demonstrates a structured backend pipeline for public data extraction work. It focuses on source traceability, validation, normalization, duplicate detection, and clean CSV/Excel deliverables.

The first MVP uses a local HTML fixture so the extraction process can be tested without depending on live websites.

## Features

- Typed property records with validation
- Text normalization helpers
- HTML directory parsing
- Duplicate record detection
- CSV and Excel exports
- Command-line interface
- Automated tests
- Linting and formatting with Ruff

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

## Methodology

See `docs/methodology.md` for collection rules, data quality rules, and current limitations.

## Status

MVP backend pipeline in progress.
