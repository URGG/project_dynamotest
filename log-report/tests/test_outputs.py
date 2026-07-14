import json
from pathlib import Path
import pytest
import re
from collections import Counter

def get_expected():
    paths, ips, total = Counter(), set(), 0
    with open("/app/access.log") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            ips.add(line.split()[0])
            m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
            if m:
                paths[m.group(1)] += 1
    return total, len(ips), paths.most_common(1)[0][0]

@pytest.fixture(scope="module")
def report_data():
    assert Path("/app/report.json").exists()
    with open("/app/report.json") as f:
        return json.load(f)

def test_total_requests(report_data):
    """Verifies Criterion 1: Calculates the total number of request lines in the log."""
    expected_total, _, _ = get_expected()
    assert report_data.get("total_requests") == expected_total

def test_unique_ips(report_data):
    """Verifies Criterion 2: Calculates the total number of unique client IP addresses."""
    _, expected_ips, _ = get_expected()
    assert report_data.get("unique_ips") == expected_ips

def test_top_path(report_data):
    """Verifies Criterion 3: Calculates the single most frequently requested path."""
    _, _, expected_path = get_expected()
    assert report_data.get("top_path") == expected_path