"""
This script demonstrates how to use the PersonConfig class to load a YAML configuration file.
"""

from pathlib import Path
from pprint import pprint

from configs import PersonConfig


if __name__ == "__main__":
    # Example usage
    # Assuming the YAML file is structured correctly.
    src_dir = Path(__file__).expanduser().resolve().parent
    project_dir = src_dir.parent
    configs_dir = project_dir / "configs"
    config_filepath = configs_dir / "person-config.yaml"
    person_config = PersonConfig.from_yaml(config_filepath)
    pprint(person_config.model_dump())
