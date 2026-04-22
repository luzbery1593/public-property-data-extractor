from app.reports.validation_report import build_validation_report
from app.schemas.property_record import PropertyRecord


def make_record(
    property_name: str = "Sample Park",
    street_address: str | None = "123 Main Street",
    city: str | None = "Orlando",
    county: str | None = "Orange County",
    zip_code: str | None = "32801",
    source_url: str = "https://example.com/sample-park",
) -> PropertyRecord:
    return PropertyRecord(
        property_name=property_name,
        street_address=street_address,
        city=city,
        state="FL",
        county=county,
        zip_code=zip_code,
        source_name="Sample Directory",
        source_url=source_url,
    )


def test_build_validation_report_counts_records() -> None:
    records = [
        make_record(),
        make_record(property_name="Lakeside Village"),
    ]

    report = build_validation_report(records)

    assert report["total_records"] == 2
    assert report["valid_records"] == 2
    assert report["duplicate_records"] == 0


def test_build_validation_report_counts_missing_fields() -> None:
    records = [
        make_record(street_address=None, city="Orlando", county=None, zip_code=None),
        make_record(property_name="Lakeside Village"),
    ]

    report = build_validation_report(records)

    assert report["missing_street_address"] == 1
    assert report["missing_city"] == 0
    assert report["missing_county"] == 1
    assert report["missing_zip_code"] == 1


def test_build_validation_report_counts_duplicates() -> None:
    records = [
        make_record(),
        make_record(source_url="https://example.com/sample-park-copy"),
    ]

    report = build_validation_report(records)

    assert report["duplicate_records"] == 1
