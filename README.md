# LiteLLM API Client

Auto-generated Python API client for [LiteLLM Proxy](https://github.com/BerriAI/litellm).

## Installation

```bash
pip install litellm-api
```

Or download from [GitHub Releases](https://github.com/gfi/litellm-api/releases).

## Usage

```python
from litellm_api import Client

client = Client(base_url="http://localhost:4000")

# Chat completion
response = client.chat_completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

## How It Works

This package is auto-generated from LiteLLM's OpenAPI spec:

1. **Extract**: Start LiteLLM proxy → fetch `/openapi.json`
2. **Generate**: Use `openapi-python-client` to create typed Python client
3. **Publish**: Build wheel → GitHub Release

## Development

### Manual Generation

```bash
# Install dependencies
pip install httpx litellm openapi-python-client build

# Extract OpenAPI spec (starts LiteLLM server temporarily)
python scripts/extract_openapi.py

# Generate client
openapi-python-client generate --path openapi.json --output-path generated-client

# Build
python -m build
```

### Triggering CI

- **Manual**: Actions → Generate and Publish → Run workflow
- **Scheduled**: Runs weekly (Monday 00:00 UTC)
- **Custom version**: Specify `litellm_version` input

## License

MIT
