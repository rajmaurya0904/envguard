"""Parse and check .env files for defined variables."""

from pathlib import Path


def parse_env_file(path: str | Path) -> dict[str, str]:
    """Parse a .env or .env.example file and return a dictionary of key-value pairs.

    Handles comments (#), whitespace, single/double quotes, and export prefixes.
    """
    env_path = Path(path)
    if not env_path.is_file():
        raise FileNotFoundError(f"Environment file not found: {env_path}")

    variables: dict[str, str] = {}

    with open(env_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and full-line comments
            if not line or line.startswith("#"):
                continue

            # Handle export prefix if present
            if line.startswith("export "):
                line = line[7:].strip()

            if "=" not in line:
                continue

            key, val = line.split("=", 1)
            key = key.strip()
            val = val.strip()

            # Remove inline comments if not inside quotes
            # A simple heuristic: if val starts with a quote, find the matching closing quote
            if val and val[0] in ('"', "'"):
                quote_char = val[0]
                end_idx = -1
                for i in range(1, len(val)):
                    if val[i] == quote_char:
                        # check if escaped
                        if i > 0 and val[i - 1] == "\\":
                            continue
                        end_idx = i
                        break
                if end_idx != -1:
                    # Everything after closing quote is ignored or comment
                    val = val[1:end_idx]
                else:
                    # Unclosed quote, take rest of val or strip trailing comment
                    val = val[1:]
            else:
                # Unquoted value, strip inline comment starting with #
                if "#" in val:
                    val = val.split("#", 1)[0].strip()

            variables[key] = val

    return variables


class EnvChecker:
    """Checker for .env and .env.example files."""

    def __init__(self, env_path: str | Path = ".env") -> None:
        self.env_path = Path(env_path)
        self.variables: dict[str, str] = {}
        if self.env_path.exists():
            self.load()

    def load(self) -> dict[str, str]:
        """Load variables from the env file."""
        self.variables = parse_env_file(self.env_path)
        return self.variables

    def get_keys(self) -> set[str]:
        """Return the set of defined environment variable keys."""
        return set(self.variables.keys())
