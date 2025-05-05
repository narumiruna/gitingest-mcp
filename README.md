# mcp-server-template

### GitHub

```json
{
  "mcpServers": {
    "mcpservertemplate": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/narumiruna/mcp-server-template",
        "mcpservertemplate"
      ]
    }
  }
}
```

### PyPI

```json
{
  "mcpServers": {
    "mcpservertemplate": {
      "command": "uvx",
      "args": ["mcpservertemplate"]
    }
  }
}
```

### Local

```json
{
  "mcpServers": {
    "mcpservertemplate": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/home/<user>/workspace/mcp-server-template",
        "mcpservertemplate"
      ]
    }
  }
}
```
