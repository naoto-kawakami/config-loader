"""This script demonstrates how to use the PersonConfig class to load a YAML configuration file."""

from pathlib import Path
from pprint import pprint

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


if __name__ == "__main__":
    # Example usage
    # Assuming the YAML file is structured correctly.
    src_dir = Path(__file__).expanduser().resolve().parent
    project_dir = src_dir.parent
    configs_dir = project_dir / "configs"
    config_filepath = configs_dir / "person-config.yaml"
    if not config_filepath.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_filepath}")

    person_config = PersonConfig.from_yaml(config_filepath)
    pprint(person_config.model_dump())
