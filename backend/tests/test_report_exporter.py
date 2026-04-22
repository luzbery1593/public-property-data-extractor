import json
from pathlib import Path

from app.exporters.report_exporter import export_report_to_json


def test_export_report_to_json_creates_file(tmp_path: Path) -> None:
    output_path = tmp_path / "validation_report.json"
    report = {
        "total_records": 2,
        "duplicate_records": 0,
    }

    result_path = export_report_to_json(report, output_path)

    assert result_path == output_path
    exported_report = json.loads(output_path.read_text(encoding="utf-8"))
    assert exported_report["total_records"] == 2
    assert exported_report["duplicate_records"] == 0
