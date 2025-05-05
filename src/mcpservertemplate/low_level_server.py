import anyio
import mcp.server.stdio
import mcp.types as types
from mcp.server.lowlevel import Server

server: Server = Server("MCP Server Template")


def add_numbers(a: float, b: float) -> str:
    return f"{a} + {b} = {a+b}"


@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="add_numbers",
            description="Add two numbers.",
            inputSchema={
                "type": "object",
                "required": ["a", "b"],
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "The first number",
                    },
                    "b": {
                        "type": "number",
                        "description": "The second number",
                    },
                },
            },
        )
    ]


@server.call_tool()
async def query_tool(
    name: str, arguments: dict
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    if name != "add_numbers":
        raise ValueError(f"Unknown tool: {name}")
    if "a" not in arguments:
        raise ValueError("Missing required argument 'a'")
    if "b" not in arguments:
        raise ValueError("Missing required argument 'b'")

    result = add_numbers(arguments["a"], arguments["b"])
    return [types.TextContent(type="text", text=str(result))]


async def run() -> None:
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


def main() -> None:
    anyio.run(run)
