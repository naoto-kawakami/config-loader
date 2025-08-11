# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

### Environment Setup

- `uv sync` - Install dependencies and create virtual environment
- `uv sync --group dev` - Install with development dependencies
- `source .venv/bin/activate` - Activate virtual environment (if needed)

### Running the Application

- `python src/main.py` - Run the main application
- `uv run python src/main.py` - Run using uv (handles environment automatically)

### Testing

- `uv run pytest` - Run all tests
- `uv run pytest tests/test_configs.py` - Run specific test file
- `uv run pytest -k "test_name"` - Run tests matching pattern
- `uv run pytest --cov` - Run tests with coverage (if pytest-cov available)

### Development

- Uses Python 3.13 (specified in `.python-version`)
- Uses `uv` for dependency management instead of pip/poetry

## Architecture Overview

This is a Python configuration loading library that uses Pydantic for data validation and PyYAML for file parsing.

### Core Components

1. **ConfigMixin** (`src/configs.py:22`) - Base mixin class that provides YAML loading functionality

   - `from_yaml()` class method loads configuration from YAML files
   - `validate_paths()` model validator automatically converts string paths to Path objects
   - Inherits from Pydantic BaseModel for validation

2. **PersonConfig** (`src/configs.py:67`) - Example configuration model

   - Demonstrates nested configuration structures
   - Shows automatic path resolution for file paths
   - Uses type hints for validation

3. **Path Resolution** (`src/configs.py:10`) - `_resolve_path()` utility
   - Expands user paths (`~`) and resolves to absolute paths
   - Used automatically by the ConfigMixin validator

### Key Patterns

- Configuration classes inherit from `ConfigMixin` to get YAML loading capability
- Path fields are automatically resolved from strings to absolute Path objects
- Nested configuration structures are supported via nested Pydantic models
- All file paths are validated and resolved during model creation

### Test Structure

- Uses pytest with parametrized tests
- Tests path resolution, YAML loading, and error handling
- `conftest.py` adds project root to Python path for imports

### Configuration Format

Example YAML structure (see `config/person-config.yaml`):

```yaml
input_filepath: ~/path/to/file.csv
output_dir: ~/path/to/output
name: John Doe
age: 30
is_student: true
nested:
  key: value
  another_key: another_value
```
