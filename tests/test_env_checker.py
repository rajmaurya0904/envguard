"""Tests for envguard.env_checker."""

from pathlib import Path

import pytest

from envguard.env_checker import EnvChecker, parse_env_file


def test_parse_env_file_basic(tmp_path: Path) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text(
        "DATABASE_URL=postgres://localhost:5432/db\n"
        "# A comment line\n"
        "API_KEY=secret123\n"
        "  INDENTED_KEY=value\n"
    )

    result = parse_env_file(env_file)
    assert result == {
        "DATABASE_URL": "postgres://localhost:5432/db",
        "API_KEY": "secret123",
        "INDENTED_KEY": "value",
    }


def test_parse_env_file_quotes_and_comments(tmp_path: Path) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text(
        'QUOTED_DOUBLE="hello world" # inline comment\n'
        "QUOTED_SINGLE='foo bar'\n"
        "EXPORTED_VAR=export_val\n"
    )

    result = parse_env_file(env_file)
    assert result == {
        "QUOTED_DOUBLE": "hello world",
        "QUOTED_SINGLE": "foo bar",
        "EXPORTED_VAR": "export_val",
    }


def test_parse_env_file_not_found(tmp_path: Path) -> None:
    missing = tmp_path / "nonexistent"
    with pytest.raises(FileNotFoundError):
        parse_env_file(missing)


def test_env_checker_class(tmp_path: Path) -> None:
    env_file = tmp_path / ".env.example"
    env_file.write_text("PORT=8080\nDEBUG=true\n")

    checker = EnvChecker(env_file)
    assert checker.get_keys() == {"PORT", "DEBUG"}
    assert checker.variables["PORT"] == "8080"
