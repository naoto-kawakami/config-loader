from pathlib import Path

import pytest

from src.mixins import YamlLoaderMixin, PathResolverMixin


class SampleConfig(YamlLoaderMixin):
    """Sample configuration class for YamlLoaderMixin."""

    name: str
    age: int
    is_student: bool


def test_yaml_loader_mixin_from_yaml(tmp_path: Path) -> None:
    """Test YamlLoaderMixin.from_yaml() method."""
    yaml_content = """
name: John Doe
age: 30
is_student: true
"""
    yaml_file = tmp_path / "test-config.yaml"
    yaml_file.write_text(yaml_content)

    config = SampleConfig.from_yaml(str(yaml_file))
    assert isinstance(config, SampleConfig)
    assert config.name == "John Doe"
    assert config.age == 30
    assert config.is_student is True


def test_yaml_loader_mixin_file_not_found() -> None:
    """Test YamlLoaderMixin.from_yaml() with non-existent file."""
    with pytest.raises(FileNotFoundError):
        SampleConfig.from_yaml("nonexistent.yaml")


class SamplePathConfig(PathResolverMixin):
    """Sample configuration class for PathResolverMixin."""

    input_file: Path
    output_dir: Path
    name: str


def test_path_resolver_mixin_converts_paths() -> None:
    """Test PathResolverMixin converts string paths to Path objects."""
    # The validator will convert strings to Path objects
    config = SamplePathConfig(
        input_file="~/test/input.txt",  # type: ignore
        output_dir="./output",  # type: ignore
        name="Test Config",
    )

    assert isinstance(config.input_file, Path)
    assert isinstance(config.output_dir, Path)
    assert config.input_file.is_absolute()
    assert config.output_dir.is_absolute()
    assert config.name == "Test Config"


def test_path_resolver_mixin_handles_none_paths() -> None:
    """Test PathResolverMixin handles None values properly."""

    class SampleOptionalPathConfig(PathResolverMixin):
        optional_path: Path | None
        name: str

    data = {
        "optional_path": None,
        "name": "Test Config",
    }

    config = SampleOptionalPathConfig(**data)
    assert config.optional_path is None
    assert config.name == "Test Config"
