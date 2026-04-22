# Public Property Data Extractor

Backend-only MVP for collecting, normalizing, validating, and exporting public property directory data from approved sources.

## Goal

Build a maintainable data extraction pipeline focused on:

- source traceability
- structured records
- data normalization
- validation
- duplicate detection
- CSV and Excel exports

## Current Scope

The first version targets a small county-level pilot instead of a nationwide dataset.

## Tech Stack

- Python
- Typer
- Pydantic
- BeautifulSoup
- Pandas
- OpenPyXL
- Pytest
- Ruff

## Repository Structure

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
data/
  samples/
exports/
