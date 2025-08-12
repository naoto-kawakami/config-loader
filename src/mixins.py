"""Configuration loading module."""

from pathlib import Path
from typing import Any, get_type_hints

import yaml
from pydantic import BaseModel, model_validator


def _resolve_path(path: str | Path) -> Path:
    """Resolve a given path string to an absolute Path object.

    Args:
        path (str | Path): Path to resolve.

    Returns:
        Path: An absolute Path object.
    """
    return Path(path).expanduser().resolve()


class YamlLoaderMixin(BaseModel):
    """Mixin class to provide YAML loading functionality."""

    @classmethod
    def from_yaml(cls, filepath: str | Path):
        """Load configuration from a YAML file.

        Args:
            filepath (str | Path): Path to the YAML file.

        Raises:
            FileNotFoundError: If the file does not exist.

        Returns:
            ConfigMixin: An instance of the class with data loaded from the YAML file.
        """
        if isinstance(filepath, str):
            filepath = Path(filepath)

        filepath = _resolve_path(filepath)
        if not filepath.exists():
            raise FileNotFoundError(f"File does not exist: {filepath}")

        with open(filepath, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        return cls(**data)


class PathResolverMixin(BaseModel):
    """Mixin class to resolve paths in configuration."""

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
                if field_type is Path and value is not None:
                    data[field_name] = _resolve_path(value)
        return data


class ConfigMixin(YamlLoaderMixin, PathResolverMixin):
    """Base configuration model that combines YAML loading and path resolution."""

    pass
