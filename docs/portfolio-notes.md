# Portfolio Notes

## Project Positioning

Public Property Data Extractor is a backend data pipeline for turning public property directory pages into clean, validated CSV and Excel deliverables.

The project is intentionally scoped as a backend MVP. It focuses on repeatable extraction, data quality, source traceability, and export reliability instead of a large live scraping target.

## Problem

Research and operations teams often need structured datasets from public directory pages, but the source data is usually inconsistent, duplicated, and difficult to verify.

This project demonstrates a maintainable process for converting semi-structured public HTML into validated records with clear source links.

## Technical Highlights

- Python CLI built with Typer
- Typed validation with Pydantic
- HTML parsing with BeautifulSoup
- Text normalization helpers
- Duplicate detection
- CSV and Excel export workflow
- Automated tests with Pytest
- Linting and formatting with Ruff
- Documented source collection rules

## Why The MVP Uses Local HTML

The first MVP uses a local HTML fixture to keep the extraction workflow repeatable and testable.

This avoids depending on unstable live websites during early development and keeps the project aligned with responsible source usage.

## What This Project Demonstrates

- Data extraction architecture
- Clean schema design
- Validation before export
- CLI-oriented backend tooling
- Testable parsing logic
- Professional Git history
- Practical data quality thinking

## Future Improvements

- Add source-specific extractors after reviewing source access rules
- Add CSV input validation
- Add richer duplicate review reports
- Add optional SQLite storage
- Add Docker support
- Add a lightweight review dashboard if a visual layer becomes useful
