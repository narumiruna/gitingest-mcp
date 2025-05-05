from typing import Annotated

from mcp.server.fastmcp import FastMCP
from pydantic import Field

# https://github.com/jlowin/fastmcp/issues/81#issuecomment-2714245145
mcp = FastMCP("MCP Server Template", log_level="ERROR")


@mcp.tool()
def add_numbers(
    a: Annotated[float, Field(description="The first number")],
    b: Annotated[float, Field(description="The second number")],
) -> str:
    """Add two numbers and return the result as a string."""
    return str(a + b)


def main():
    mcp.run()
