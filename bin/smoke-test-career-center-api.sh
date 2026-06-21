#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${CAREER_CENTER_API_URL:-http://127.0.0.1:8000}"
APP_ID="${CAREER_CENTER_TEST_APP_ID:-application-broadridge-product-analyst-2026-v1}"

echo "Smoke testing Career Center API at: $BASE_URL"
echo "Test application: $APP_ID"
echo

check() {
  local name="$1"
  local url="$2"

  echo "==> $name"
  status="$(curl -s -o /tmp/career-center-smoke-response.json -w "%{http_code}" "$url")"

  if [ "$status" != "200" ]; then
    echo "FAIL: $name returned HTTP $status"
    cat /tmp/career-center-smoke-response.json
    echo
    exit 1
  fi

  echo "PASS: $name"
  echo
}

check "GET /health" "$BASE_URL/health"
check "GET /applications" "$BASE_URL/applications"
check "GET /applications/{id}" "$BASE_URL/applications/$APP_ID"
check "GET /applications/{id}/jd" "$BASE_URL/applications/$APP_ID/jd"
check "GET /applications/{id}/artifacts" "$BASE_URL/applications/$APP_ID/artifacts"

echo "All smoke tests passed."
