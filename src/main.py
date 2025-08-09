"""This script demonstrates how to use the PersonConfig class to load a YAML configuration file."""

from configs import PersonConfig


if __name__ == "__main__":
    # Example usage
    # Assuming the YAML file is structured correctly and exists at the specified path
    person_config = PersonConfig.from_yaml("../config/person-config.yaml")
    print(person_config)
