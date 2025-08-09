from pathlib import Path

import pytest

from src.configs import PersonConfig, _resolve_path


@pytest.mark.parametrize(
    "input_path,expected_name",
    [
        ("~/test_dir/file.txt", "file.txt"),
        ("./test_configs.py", "test_configs.py"),
    ],
)
def test_resolve_path_expands_user_and_resolves(
    input_path: str,
    expected_name: str,
) -> None:
    resolved = _resolve_path(input_path)
    assert resolved.name == expected_name
    assert resolved.is_absolute()


@pytest.fixture
def expected_person_data() -> dict:
    return {
        "name": "John Doe",
        "age": 30,
        "is_student": True,
        "input_filepath_name": "john_doe.csv",
        "nested": {
            "key": "value",
            "another_key": "another_value",
        },
    }


@pytest.fixture
def sample_yaml_content() -> str:
    return """
input_filepath: ~/dev/config-loader/data/input/john_doe.csv
output_dir: ~/dev/config-loader/data/output
name: John Doe
age: 30
is_student: true
nested:
  key: value
  another_key: another_value
"""


def test_person_config_from_yaml(
    tmp_path: Path,
    sample_yaml_content: str,
    expected_person_data: dict,
) -> None:
    yaml_file = tmp_path / "person-config.yaml"
    yaml_file.write_text(sample_yaml_content)
    config = PersonConfig.from_yaml(str(yaml_file))
    assert isinstance(config, PersonConfig)
    assert config.name == expected_person_data["name"]
    assert config.age == expected_person_data["age"]
    assert config.is_student is expected_person_data["is_student"]
    assert isinstance(config.input_filepath, Path)
    assert config.input_filepath.name == expected_person_data["input_filepath_name"]
    assert config.nested.key == expected_person_data["nested"]["key"]
    assert config.nested.another_key == expected_person_data["nested"]["another_key"]


@pytest.mark.parametrize("bad_path", ["nonexistent.yaml", "./notfound.yaml"])
def test_file_not_found(bad_path: str) -> None:
    with pytest.raises(FileNotFoundError):
        PersonConfig.from_yaml(bad_path)
