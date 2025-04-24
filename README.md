# MCP Server

This is a simple Model Context Protocol (MCP) server implementation that exposes several utility functions as tools.

## Purpose
Andi's personal MCP server test on glama.ai / Used in cursor with:
```
pip install "mcp[cli]"
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