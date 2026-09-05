#!/usr/bin/env python3
"""Small dependency-free smoke test for local development."""

from __future__ import annotations

import argparse
import json
import time
from urllib.error import URLError
from urllib.request import Request, urlopen


def get_json(url: str) -> tuple[int, dict]:
    request = Request(url, headers={"Origin": "http://127.0.0.1:5500"})
    with urlopen(request, timeout=2) as response:
        return response.status, json.load(response)


def get_text(url: str) -> tuple[int, str]:
    with urlopen(url, timeout=2) as response:
        return response.status, response.read().decode("utf-8")


def wait_for(check, label: str) -> None:
    deadline = time.monotonic() + 10
    last_error = None
    while time.monotonic() < deadline:
        try:
            check()
            return
        except (AssertionError, URLError, TimeoutError) as error:
            last_error = error
            time.sleep(0.1)
    raise RuntimeError(f"Timed out waiting for {label}: {last_error}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-url", default="http://127.0.0.1:8000")
    parser.add_argument("--web-url", default="http://127.0.0.1:5500")
    args = parser.parse_args()

    def check_api() -> None:
        status, payload = get_json(f"{args.api_url}/api/v1/courses")
        assert status == 200
        assert payload["status"] == "success"
        assert payload["data"]

    def check_web() -> None:
        status, html = get_text(args.web_url)
        assert status == 200
        assert "AGMA.io - Learn Without Limits" in html
        assert "/api/v1/courses" in html

    wait_for(check_api, "the platform API")
    wait_for(check_web, "the company website")
    print("Smoke checks passed: company web and platform API")


if __name__ == "__main__":
    main()
