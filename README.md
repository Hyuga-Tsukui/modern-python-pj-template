# Modern Python Development Project Template

This project is a template for modern Python development with a strong emphasis on type safety.
Supporting Python 3.13 and above, it integrates the latest tools and strict type checking to facilitate high-quality code development.

## Features

- **Type Safety Focused**: Strict static type checking with mypy (`strict = true` mode)
- **Modern Python**: Support for Python 3.13 and above
- **Code Quality Tools**:
  - Ruff: Fast linter and formatter
  - mypy: Advanced type checking
- **Modern Dependency Management**: Fast dependency management using uv
- **Simple Development Commands**: Consistent development experience via Makefile

## Setting Up the Development Environment

```bash
# Install dependencies
make install
```

## Development Commands

```bash
# Format code
make fmt

# Lint (code quality check and type check)
make lint

# List all commands
make help
```

## About Type Safety

This template maximizes Python's type hint capabilities and performs strict type checking with mypy:

- `disallow_untyped_defs = true`: Requires type annotations for all functions
- `disallow_any_generics = true`: Prohibits `Any` in generic types
- `check_untyped_defs = true`: Checks functions even without type annotations
- `warn_return_any = true`: Warns when a function returns `Any`

Static analysis is also performed with Ruff to maintain coding standards and consistent code style.
