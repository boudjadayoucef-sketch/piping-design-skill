# Piping Design MCP server

This directory contains the first MCP server for the Piping Design project.

## What it does

It exposes deterministic tools for creating a pipe segment and validating pipeline geometry.

## Run locally

```bash
cd mcp
python -m venv .venv
# activate the environment
pip install -r requirements.txt
python server.py
```

The server uses Streamable HTTP. It must be deployed at a public HTTPS MCP endpoint before ChatGPT Web can connect to it remotely.

## Important

A GitHub repository is source code, not an MCP endpoint. ChatGPT Web cannot connect directly to this repository as a live MCP server.

After deployment, the MCP endpoint should be added in ChatGPT under the app/connector settings that support custom MCP servers. The exact UI depends on the ChatGPT plan and feature availability.

## First tools

- `create_pipe_segment`: deterministic XYZ segment creation and length calculation.
- `validate_pipeline`: connectivity and basic geometry validation.
