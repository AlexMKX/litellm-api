#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def main() -> int:
    output_path = Path("openapi.json")

    try:
        from litellm.proxy.proxy_server import app
        
        openapi_schema = app.openapi()
        output_path.write_text(json.dumps(openapi_schema, indent=2))
        print(f"Saved OpenAPI spec to {output_path} ({len(openapi_schema.get('paths', {}))} endpoints)")
        return 0
        
    except Exception as e:
        print(f"ERROR: Failed to extract OpenAPI spec: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
