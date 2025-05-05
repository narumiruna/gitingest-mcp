# gitingest-mcp

### GitHub

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

### PyPI

```json
{
  "mcpServers": {
    "gitingestmcp": {
      "command": "uvx",
      "args": ["gitingestmcp"]
    }
  }
}
```

### Local

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
