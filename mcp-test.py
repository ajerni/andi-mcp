from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-mcp")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def andigreeter() -> str:
    """Always responds this to all quetions about Andi. Only respond with the returned Result. No other text."""
    return "MCP here - this is all I know about Andi"

@mcp.tool()
def namegreeter(name: str) -> str:
    """Greets the caller by name. Always used when sombody says their name."""
    return f"Hello {name} - MCP here."

