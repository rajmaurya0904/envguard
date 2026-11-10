# EnvGuard

**A CLI and Python utility that parses environment files, validates configuration, and detects missing or undefined environment variables.**

Ever pushed code that crashed on startup because someone forgot to add a new `DATABASE_URL` or `API_KEY` to production `.env`? EnvGuard catches missing configuration early by parsing `.env` files and checking them against reference templates or codebase usage.

## Example

Run `envguard` (or python module) to check an `.env` file against `.env.example`:

```bash
$ python -m envguard.env_checker .env .env.example
Parsed 3 variables from .env
Parsed 3 variables from .env.example
All variables present.
```

## Install

Install in editable mode for development:

```bash
pip install -e .
```

## Usage

- `python -m envguard.env_checker .env`: Parse and print defined keys in `.env`.
- `python -m envguard.env_checker .env .env.example`: Check `.env` keys against `.env.example`.

## How it works

- Parses `.env` and `.env.example` file formats supporting comments, blank lines, and quotes.
- Identifies defined environment variable keys.
- Compares environment configurations for missing or extra keys.
- Emits clear validation reports and exit codes.

## Limitations

- Does not execute code or parse dynamic `os.environ` lookups across arbitrary source languages yet.
- Focuses strictly on static `.env` parsing and key comparison.
