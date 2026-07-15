#!/bin/bash
mkdir -p /logs/verifier

pytest "$(dirname "$0")/test_outputs.py" --tb=short
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo "1.0" > /logs/verifier/reward.txt
    cat << 'EOF' > /logs/verifier/ctrf.json
{
  "results": {
    "tool": {"name": "harbor-verifier"},
    "summary": {"tests": 3, "passed": 3, "failed": 0, "pending": 0, "skipped": 0, "other": 0},
    "tests": [
      {"name": "test_total_requests", "status": "passed"},
      {"name": "test_unique_ips", "status": "passed"},
      {"name": "test_top_path", "status": "passed"}
    ]
  }
}
EOF
else
    echo "0.0" > /logs/verifier/reward.txt
    cat << 'EOF' > /logs/verifier/ctrf.json
{
  "results": {
    "tool": {"name": "harbor-verifier"},
    "summary": {"tests": 3, "passed": 0, "failed": 3, "pending": 0, "skipped": 0, "other": 0},
    "tests": [
      {"name": "Log parsing validation", "status": "failed", "message": "Calculated metrics do not match expected log criteria."}
    ]
  }
}
EOF
fi