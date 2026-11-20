# AGENTS.md

## Public interface

The public interface is the `cat-data-tools` Typer CLI (`cat_data_tools.cli:app`, declared in `pyproject.toml` under `[tool.flit.scripts]`) and the functions re-exported from `cat_data_tools/__init__.py`; `DOCS.md` lists every command and exported function. The re-exported command functions are documented once, as commands.

## Setup

- `make install` performs an editable install with flit; `make setup` is `make clean` plus install. Python >= 3.9; runtime dependencies are only numpy, pandas and typer[all].
- Docker is the CI path: `docker build --tag islasgeci/cat_data_tools:latest .`, then `docker compose run --rm islasgeci`. The service is named `islasgeci`, not `cat_data_tools`; `islasgeci_dev` builds `Dockerfile.dev` on top of the `latest` image and installs the OpenCode CLI.
- Test tooling (black, flake8, mypy, mutmut, pylint, pytest) is installed by `Dockerfile`, not declared in `pyproject.toml`; `make check` needs those executables on PATH. `make check` does not run pylint; only `make linter` does.
- CI (`.github/workflows/actions.yml`) runs only on pushes to `develop`: it builds the image, runs `make check`, `make coverage` and `make mutants`, then pushes to Docker Hub and PyPI.

## Commands

- `make check` runs black (`--line-length 100`) and flake8 (`--max-line-length 100`) on `cat_data_tools` and `tests`, then mypy on both. Run it before tests.
- `make tests` runs pytest from the repo root; fixtures are addressed as `tests/data/...`, so running from another directory fails.
- `make coverage` runs pytest with `--cov` plus `coverage report`; it leaves `coverage.xml` at the root.
- `make mutants` runs mutmut; `make all` is check + coverage + mutants. The trailing `expr` gate in the Makefile always exits 1, so read `mutmut results` itself.
- `make red`, `make green`, `make refactor` drive the TDD loop and commit with emoji messages; on failure `red` restores the tests, `green` restores `cat_data_tools/*.py`, and `refactor` restores both, discarding uncommitted edits.
- `make init` adds the repo as a git safe directory, sets the GECI identity, then runs setup and tests.

## Conventions

- Column names at the edges are Spanish (`Fecha`, `Esfuerzo`, `Capturas`, `Tramperos`), except `write-trap-check-log`, which writes English headers. Commands translate `Fecha`/`Date` (and, for monthly summaries, `Effort`/`Esfuerzo`, `Total_individuals`/`Capturas`) at entry and restore Spanish headers on output; keep that boundary instead of changing summary logic.
- Trap status codes: `X` = capture, `A` = active, `R`/`RX` = checked; zone is the part of `ID` before the first `-`.
- `write-trap-daily-status` requires `--island Socorro|Guadalupe` (Guadalupe also deduplicates on `Trapper` because positions repeat) and a JSON config with `days_active`.
- New commands go in `cli.py` as `@app.command()` and must be added to the explicit import list in `__init__.py`; there is no wildcard import.
- Release steps: bump `__version__`, add a `CHANGELOG.md` entry, and update the version string asserted in `tests/test_cli.py`. The CI workflow only touches the `latest` tag; version tags are added by hand (none exists for 1.5.0), so `git diff v1.4.0..HEAD` spans more than one release.

## Testing notes

- `tests/test_cli.py` drives commands with `typer.testing.CliRunner` and asserts output headers and row counts; scratch CSVs are written into `tests/` and usually removed by the same test.
- `write-trap-daily-status` fixtures are `tests/data/check_traps_log.csv` (English headers) and a Spanish-dates copy created inside the test; `tests/data/trap_daily_status_config.json` sets `days_active` to 15.
- A few test functions are named `tests_*`; pytest still collects them because the default `python_functions` pattern is `test*`.
