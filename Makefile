lint:
	uv run ruff check .

type:
	uv run mypy --install-types --non-interactive .

test:
	uv run pytest -v -s --cov=src tests

publish:
	uv build -f wheel
	uv publish

dev:
	uv run mcp dev src/gitingestmcp/server.py

.PHONY: lint test publish
