"""This script demonstrates how to use the PersonConfig class to load a YAML configuration file."""

from pathlib import Path

from configs import PersonConfig


if __name__ == "__main__":
    # Example usage
    # Assuming the YAML file is structured correctly.
    src_dir = Path(__file__).expanduser().resolve().parent
    project_dir = src_dir.parent
    config_dir = project_dir / "config"
    config_filepath = config_dir / "person-config.yaml"
    if not config_filepath.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_filepath}")

    person_config = PersonConfig.from_yaml(config_filepath)
    print(person_config)
