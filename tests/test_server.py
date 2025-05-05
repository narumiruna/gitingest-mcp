import pytest
from mcp import ClientSession
from mcp import StdioServerParameters
from mcp import stdio_client
from mcp.types import TextContent


@pytest.fixture
def server_params() -> StdioServerParameters:
    return StdioServerParameters(command="uv", args=["run", "mcpservertemplate"])


@pytest.mark.asyncio
async def test_list_tools(server_params: StdioServerParameters) -> None:
    async with stdio_client(server_params) as (read, write), ClientSession(read, write) as session:
        await session.initialize()

        result = await session.list_tools()
        assert len(result.tools) > 0


@pytest.mark.asyncio
async def test_call_tool(server_params: StdioServerParameters) -> None:
    async with stdio_client(server_params) as (read, write), ClientSession(read, write) as session:
        await session.initialize()

        a = 1234
        b = 5678
        result = await session.call_tool("add_numbers", {"a": a, "b": b})

        assert len(result.content) == 1
        assert isinstance(result.content[0], TextContent)
        assert float(result.content[0].text) == a + b
