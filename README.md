# MCP Server

This is a simple Model Context Protocol (MCP) server implementation that exposes several utility functions as tools.
Andi's personal MCP server.

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency management. To install the dependencies:

```bash
uv pip install -r requirements.txt
```

If you don't have uv installed, you can install it with:

```bash
curl -sSf https://astral.sh/uv/install.sh | bash
```

## Usage

Run the server:

```bash
python mcp-test.py
```

## Available Tools

The server provides the following tools:
- `add`: Add two numbers
- `multiply`: Multiply two numbers
- `andigreeter`: Responds with information about Andi
- `namegreeter`: Greets a user by name

## Custom Development

To add more tools, simply define new functions with the `@mcp.tool()` decorator:

```python
@mcp.tool()
def your_function(param1: type, param2: type) -> return_type:
    """Description of your function"""
    # Your code here
    return result
``` 