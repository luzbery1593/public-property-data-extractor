from pathlib import Path

import pytest

from app.extractors.sample_directory import (
    extract_sample_directory,
    parse_city_state_zip,
)


def test_parse_city_state_zip_returns_parts() -> None:
    city, state, zip_code = parse_city_state_zip("Orlando, FL 32801")

    assert city == "Orlando"
    assert state == "FL"
    assert zip_code == "32801"


def test_parse_city_state_zip_rejects_invalid_text() -> None:
    with pytest.raises(ValueError):
        parse_city_state_zip("Orlando Florida 32801")


def test_extract_sample_directory_returns_property_records() -> None:
    fixture_path = Path("tests/fixtures/sample_directory.html")

    records = extract_sample_directory(
        html_path=fixture_path,
        base_url="https://example.com",
    )

    assert len(records) == 2
    assert records[0].property_name == "Sample Mobile Home Park"
    assert records[0].source_url.unicode_string() == (
        "https://example.com/sample-mobile-home-park"
    )
    assert records[1].property_name == "Lakeside Village"
    assert records[1].source_url.unicode_string() == (
        "https://example.com/lakeside-village"
    )
