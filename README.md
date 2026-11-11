# EnvGuard

**A CLI and Python utility that parses environment files, validates configuration, and detects missing or undefined environment variables.**

AI-generated code and legacy codebases frequently introduce scattered, undocumented environment variable dependencies across configuration files and source code without updating deployment `.env` templates. EnvGuard eliminates deployment crashes and configuration drift by statically parsing `.env` files and verifying environment variable completeness against reference templates before code reaches production.

## Example

Run `envguard` to check an `.env` file against `.env.example`:

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
