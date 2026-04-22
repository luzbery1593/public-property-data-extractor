import pytest

from app.normalizers.text import (
    normalize_optional_text,
    normalize_required_text,
    normalize_whitespace,
)


def test_normalize_whitespace_collapses_spaces() -> None:
    assert normalize_whitespace("  Sample   Property\nName  ") == "Sample Property Name"


def test_normalize_whitespace_returns_none_for_empty_text() -> None:
    assert normalize_whitespace("   ") is None


def test_normalize_optional_text_accepts_none() -> None:
    assert normalize_optional_text(None) is None


def test_normalize_required_text_rejects_empty_text() -> None:
    with pytest.raises(ValueError):
        normalize_required_text("   ")
