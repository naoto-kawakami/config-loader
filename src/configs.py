"""Configuration loading module."""

from pathlib import Path
from typing import Any, get_type_hints

import yaml
from pydantic import BaseModel, model_validator


def _resolve_path(path: str) -> Path:
    """Resolve a given path string to an absolute Path object.

    Args:
        path (str): Path string to resolve.

    Returns:
        Path: An absolute Path object.
    """
    return Path(path).expanduser().resolve()


class ConfigMixin:
    """Mixin class to provide configuration loading functionality."""

    @classmethod
    def from_yaml(cls, filepath_text: str):
        """Load configuration from a YAML file.

        Args:
            filepath_text (str): Path to the YAML file.

        Raises:
            FileNotFoundError: If the file does not exist.

        Returns:
            ConfigMixin: An instance of the class with data loaded from the YAML file.
        """
        filepath = _resolve_path(filepath_text)
        if not filepath.exists():
            raise FileNotFoundError(f"File does not exist: {filepath}")

        with open(filepath, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        return cls(**data)

    @model_validator(mode="before")
    @classmethod
    def validate_paths(cls, data: Any) -> Any:
        """Convert string paths in the data to Path objects.

        Args:
            data (Any): Data to validate and convert.

        Returns:
            Any: Data with string paths converted to Path objects, if applicable.
        """
        if isinstance(data, dict):
            type_hints = get_type_hints(cls)
            for field_name, value in data.items():
                field_type = type_hints.get(field_name)
                if field_type == Path and value is not None:
                    data[field_name] = _resolve_path(value)
        return data


class PersonConfig(ConfigMixin, BaseModel):
    """Configuration model for a person with nested structures."""

    class Nested(BaseModel):
        """Nested configuration model."""
        key: str
        another_key: str

    input_filepath: Path
    output_dir: Path
    name: str
    age: int
    is_student: bool
    nested: Nested
