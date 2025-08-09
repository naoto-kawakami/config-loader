
# config-loader

A simple Python project for loading configuration files.

## Features
- Loads YAML configuration files
- Easy to extend for other formats
- Minimal dependencies

## Getting Started

### Prerequisites
- Python 3.13 (see `.python-version`)
- [uv](https://github.com/astral-sh/uv) for dependency and environment management


### Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/config-loader.git
   cd config-loader
   ```

2. Install all dependencies and create the virtual environment (if not already present) with:
   ```sh
   uv sync
   ```
   This will use Python 3.13 if installed, as specified in `.python-version`, and create `.venv` automatically.
3. Activate the virtual environment:
   ```sh
   source .venv/bin/activate
   ```

### Usage
Run the main script:
```sh
python src/main.py
```

You can modify the configuration in `config/person-config.yaml`.

## Development
To install development dependencies:
```sh
uv sync --group dev
```

## Project Structure
```
config-loader/
├── .python-version
├── config-loader.code-workspace
├── pyproject.toml
├── README.md
├── uv.lock
├── config/
│   └── person-config.yaml
├── src/
│   ├── configs.py
│   └── main.py
```

## License
MIT
