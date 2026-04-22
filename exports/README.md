# Exports

This directory is used for generated CSV and Excel outputs.

Generated files are intentionally ignored by Git and should not be committed to the repository.

Run the CLI commands from `backend/` to create local export files:

```bash
property-extractor export-sample-directory
property-extractor import-florida-health --input ../data/raw/florida_mobile_home_rv_parks.xls
```

Expected generated files include:

```text
sample_directory_records.csv
sample_directory_records.xlsx
florida_health_records.csv
florida_health_records.xlsx
```
