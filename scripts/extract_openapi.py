#!/usr/bin/env python3
"""Extract OpenAPI spec from LiteLLM proxy server."""

import json
import subprocess
import sys
import time
from pathlib import Path

import httpx


def wait_for_server(url: str, timeout: int = 60) -> bool:
    """Wait for server to be ready."""
    start = time.time()
    while time.time() - start < timeout:
        try:
            resp = httpx.get(url, timeout=5.0)
            if resp.status_code == 200:
                return True
        except httpx.RequestError:
            pass
        time.sleep(1)
    return False


def main() -> int:
    output_path = Path("openapi.json")
    litellm_port = 4000
    health_url = f"http://localhost:{litellm_port}/health"
    openapi_url = f"http://localhost:{litellm_port}/openapi.json"

    print("Starting LiteLLM proxy server...")
    proc = subprocess.Popen(
        ["litellm", "--port", str(litellm_port)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    try:
        print(f"Waiting for server at {health_url}...")
        if not wait_for_server(health_url, timeout=120):
            print("ERROR: Server failed to start", file=sys.stderr)
            return 1

        print(f"Fetching OpenAPI spec from {openapi_url}...")
        resp = httpx.get(openapi_url, timeout=30.0)
        resp.raise_for_status()

        spec = resp.json()
        output_path.write_text(json.dumps(spec, indent=2))
        print(f"Saved OpenAPI spec to {output_path} ({len(spec.get('paths', {}))} endpoints)")
        return 0

    finally:
        print("Stopping server...")
        proc.terminate()
        proc.wait(timeout=10)


if __name__ == "__main__":
    sys.exit(main())
