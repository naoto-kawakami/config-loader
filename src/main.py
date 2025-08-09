"""This script demonstrates how to use the PersonConfig class to load a YAML configuration file."""

from pathlib import Path

from configs import PersonConfig


if __name__ == "__main__":
    # Example usage
    # Assuming the YAML file is structured correctly.
    filepath = Path("../config/person-config.yaml").expanduser().resolve()
    if not filepath.exists():
        raise FileNotFoundError(f"Configuration file not found: {filepath}")

    person_config = PersonConfig.from_yaml("../config/person-config.yaml")
    print(person_config)
