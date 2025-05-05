from typing import Annotated

from gitingest import ingest_async
from mcp.server.fastmcp import FastMCP
from pydantic import Field

# https://github.com/jlowin/fastmcp/issues/81#issuecomment-2714245145
mcp = FastMCP("Gitingest MCP Server", log_level="ERROR")


@mcp.tool()
async def ingest_git(
    source: Annotated[
        str,
        Field(
            description="The source to analyze, which can be a URL (for a Git repository) or a local directory path."
        ),
    ],
    max_file_size: Annotated[
        int,
        Field(
            description=(
                "Maximum allowed file size for file ingestion."
                "Files larger than this size are ignored, by default 10*1024*1024 (10 MB)."
            )
        ),
    ] = 10 * 1024 * 1024,
    include_patterns: Annotated[
        str,
        Field(description="Pattern or set of patterns specifying which files to include, e.q. '*.md, src/'"),
    ] = "*.md",
    exclude_patterns: Annotated[
        str,
        Field(description="Pattern or set of patterns specifying which files to exclude, e.q. '*.md, src/'"),
    ] = "src/",
    branch: Annotated[str, Field(description="The branch to clone and ingest.")] = "main",
    return_content: Annotated[bool, Field(description="Whether to return the content of the files.")] = False,
) -> str:
    """
    This function analyzes a source (URL or local path), clones the corresponding repository (if applicable),
    and processes its files according to the specified query parameters.
    It can return a summary, a tree-like structure of the files, or the content of the files.
    """
    summary, tree, content = await ingest_async(
        source,
        max_file_size=max_file_size,
        include_patterns=include_patterns,
        exclude_patterns=exclude_patterns,
        branch=branch,
    )

    if return_content:
        return content
    return f"summary: {summary}\ntree: {tree}"


def main() -> None:
    mcp.run()
