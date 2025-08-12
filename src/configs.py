"""
This module defines configuration models using Pydantic for structured data validation.
It includes mixins for loading configurations from YAML files and resolving paths.
"""

from pathlib import Path

from mixins import ConfigMixin


class PersonConfig(ConfigMixin):
    """Configuration model for a person with nested structures."""

    class Nested(ConfigMixin):
        """Nested configuration model."""

        key: str
        another_key: str

    input_filepath: Path
    output_dir: Path
    name: str
    age: int
    is_student: bool
    nested: Nested
