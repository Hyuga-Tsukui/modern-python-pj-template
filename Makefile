lint: ## Run linters ruff and mypy
	@ruff check --fix
	@mypy .

fmt: ## Run ruff formatter
	@ruff format

install: ## Install dependencies
	@uv sync

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		sed 's/:.*## /: /' | \
		awk 'BEGIN {FS = ": "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
