# Piping Design MCP server

This directory contains the remote MCP server for the Piping Design project.

## What it does

It exposes deterministic tools for creating pipe segments and validating pipeline geometry.

## Run locally

From the repository root:

```bash
python -m venv .venv
# activate the environment
pip install -r mcp/requirements.txt
python -m mcp.server
```

The server uses Streamable HTTP and listens on `0.0.0.0:$PORT` (default `8000`).

## Remote deployment

A hosting service must provide:

- Python 3.11+;
- build command: `pip install -r mcp/requirements.txt`;
- start command: `python -m mcp.server`;
- a public HTTPS URL;
- the host-provided `PORT` environment variable.

GitHub is the source repository; it is not itself a live MCP endpoint.

After deployment, add the resulting public MCP endpoint to an MCP-capable ChatGPT app/connector if that capability is available on the account.

## Tools

- `create_pipe_segment`: deterministic XYZ segment creation and length calculation.
- `validate_pipeline`: connectivity and basic geometry validation.

## Security

Do not put secrets in this repository. Authentication should be added before exposing project data or write operations publicly.
