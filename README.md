# Language wallpaper

### A simple python application that updates your desktop background with a phrase and its translation.

___

## Available scripts

All actions that are used in the repository are available in the Makefile.
All pre-commit hooks, GitHub workflows, and build tooling use this Makefile to perform these actions.
This allows for DRY, self-documentation, and easy manual running.

The following Makefile commands are available for this repository:

### `make install`

Installs the application.

### `make update`
Update all the dependencies to the latest available version.

### `make start`
Runs main.py

### `make test-unit`
Runs unit tests and build a coverage report

### `make check-all`
Runs all code style and security checks

### `make check-format`
Checks formatting

### `make check-poetry`
Checks the lock file is up to date

### `make check-lint`
Checks for any linting errors

### `make check-mypy`
Checks static typing

### `make check-bandit`
Checks for security vulnerabilities in the file.

### `make check-private-keys`
Checks for the any hardcoded string that could be private keys.

### `make check-format`
Checks for any formatting errors

### `make format`
Re-formats all files
