# Python project boilerplate

A boilerplate for generic Python3 projects. Files (i.e. `setup.py`, `tox.ini`) required for
publishing packages or multi-environment testing are not included. Because there are projects that
run only in a specific environment and are not meant for distribution. The goal is to create a
starting template that enforces coding styles and aligns with the best practices as much as
possible.

## Installation

Use the package manager `pipenv`.

```bash
pipenv install --dev
pre-commit install
```

## Usage

```python
print("Code example")
```
