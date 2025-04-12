lint: ## Run linters ruff and mypy
	@uv run ruff check --fix
	@uv run mypy .

fmt: ## Run ruff formatter
	@uv run ruff format

install: ## Install dependencies
	@uv sync

dev-server: ## Django migrate 
	@uv run manage.py runserver

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		sed 's/:.*## /: /' | \
		awk 'BEGIN {FS = ": "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
