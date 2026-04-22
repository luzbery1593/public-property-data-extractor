import re
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from app.normalizers.text import normalize_optional_text, normalize_required_text
from app.schemas.property_record import PropertyRecord

CITY_STATE_ZIP_PATTERN = re.compile(
    r"^(?P<city>.*?),\s*(?P<state>[A-Za-z]{2})\s*(?P<zip_code>\d{5}(?:-\d{4})?)?$"
)


def parse_city_state_zip(value: str) -> tuple[str | None, str, str | None]:
    match = CITY_STATE_ZIP_PATTERN.match(value.strip())
    if match is None:
        raise ValueError("city_state_zip must match 'City, ST ZIP'")

    city = normalize_optional_text(match.group("city"))
    state = normalize_required_text(match.group("state")).upper()
    zip_code = normalize_optional_text(match.group("zip_code"))

    return city, state, zip_code


def extract_sample_directory(
    html_path: Path,
    base_url: str,
    source_name: str = "Sample Directory",
) -> list[PropertyRecord]:
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    records: list[PropertyRecord] = []

    for card in soup.select(".property-card"):
        name_element = card.select_one(".property-name")
        address_element = card.select_one(".street-address")
        city_state_zip_element = card.select_one(".city-state-zip")
        county_element = card.select_one(".county")
        link_element = card.select_one(".property-link")

        if (
            name_element is None
            or city_state_zip_element is None
            or link_element is None
        ):
            continue

        city, state, zip_code = parse_city_state_zip(city_state_zip_element.get_text())

        records.append(
            PropertyRecord(
                property_name=normalize_required_text(name_element.get_text()),
                street_address=normalize_optional_text(
                    address_element.get_text() if address_element else None
                ),
                city=city,
                state=state,
                county=normalize_optional_text(
                    county_element.get_text() if county_element else None
                ),
                zip_code=zip_code,
                source_name=source_name,
                source_url=urljoin(base_url, link_element.get("href", "")),
            )
        )

    return records
