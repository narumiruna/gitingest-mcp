# gitingest-mcp

A Model Context Protocol (MCP) server implementation that integrates with [gitingest](https://github.com/cyclotruc/gitingest) for Git repository analysis and ingestion. This server allows AI models to efficiently access and analyze code repositories through a standardized interface.

## Features

- Easy integration with AI assistants through the Model Context Protocol
- Git repository analysis and ingestion capabilities
- Support for filtering files by size, patterns, and branches
- Returns comprehensive repository information including summaries, file structure, and content

## Installation

### Using pip/uv

```bash
pip install gitingestmcp
# or with uv
uv pip install gitingestmcp
```

## Usage

### Configuration Options

Add the following configuration to your AI assistant's settings to enable gitingest-mcp as an MCP server:

#### PyPI Installation

```json
{
  "mcpServers": {
    "gitingestmcp": {
      "command": "uvx",
      "args": ["-U", "gitingestmcp"]
    }
  }
}
```

#### GitHub Installation

```json
{
  "mcpServers": {
    "gitingestmcp": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/narumiruna/gitingest-mcp",
        "gitingestmcp"
      ]
    }
  }
}
```

#### Local Installation

```json
{
  "mcpServers": {
    "gitingestmcp": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/home/<user>/workspace/gitingest-mcp",
        "gitingestmcp"
      ]
    }
  }
}
```

## API

The server provides the following tool:

### `ingest_git`

Analyzes a Git repository and returns its content in a structured format.

#### Parameters:

- `source`: The URL of a Git repository or a local directory path
- `max_file_size` (optional): Maximum allowed file size in bytes (default: 10MB)
- `include_patterns` (optional): Pattern or set of patterns specifying files to include (e.g., "\*.md, src/")
- `exclude_patterns` (optional): Pattern or set of patterns specifying files to exclude
- `branch` (optional): The branch to clone and analyze (default: "main")

#### Returns:

A string containing:

1. Repository summary
2. Tree-like structure of the files
3. Content of the repository files

## Resources

- gitingest website: https://gitingest.com/
- gitingest repository: https://github.com/cyclotruc/gitingest

## License

See the [LICENSE](LICENSE) file for details.
