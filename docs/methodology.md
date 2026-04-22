# Methodology

This project collects and structures public property directory data only from approved and publicly accessible sources.

## Collection Rules

- Use public pages that do not require authentication.
- Respect source terms of use.
- Do not bypass access controls or restricted areas.
- Store the source URL with each collected record.
- Leave missing fields blank instead of guessing.

## MVP Data Fields

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

## Data Quality Rules

- Normalize whitespace.
- Standardize state values.
- Validate source URLs.
- Detect likely duplicates before final export.
- Export clean CSV and Excel files.

## Current Limitations

- The current extractor uses a local HTML fixture for repeatable testing.
- Live source collection is intentionally not included in the first MVP.
- New sources should be added only after reviewing their access rules and structure.
