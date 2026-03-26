# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Fixed

### Changed

### Removed

## [1.2.0] - 2026-03-26
- CLI command `write-posterior-samples-summary`. This function receives the posterior samples of `eradications_stan` model and writes a summary of the samples in a json file.

## [1.1.0] - 2026-03-24
### Added
- CLI command `write-trap-check-log`. This command receives a splitted daily positions and returns only the list of traps checked.

## [1.0.2] - 2026-03-09
### Fixed
- The function `summarize_effort_captures_and_add_trappers()` now joins the number of trappers by date, not by row.
## [1.0.1] - 2026-03-05
### Fixed
- Date column adapter in CLI commands `write-trap-daily-status` and `write-daily-effort-and-captures-summary-by-zone`. Now can receive Spanish and English date column names, and always returns them in Spanish.

## [1.0.0] - 2026-03-04
### Added
- CLI command `write-daily-effort-and-captures-summary-by-zone`.
- CLI command `write-trap-daily-status`.

### Removed
- Deprecated function `join-captures-with-traps-info` commands.

## [0.11.0] - 2026-02-24
### Added
- CLI command `write-effort-captures-as-json` to write effort captures as required by Stan.

### Changed
- Deprecation warnings for `join-captures-with-traps-info` commands. These commands will be removed in the next major release.

## [0.10.0] - 2025-06-04
### Added
- Add cli command `join-traps-positions-and-active-traps-by-id-and-line`

## [0.9.2] - 2025-05-08

### Fixed
- Cli command `update-status-traps` order properly and keeps first ocurrence and changes in type of traps

## [0.9.1] - 2025-05-07

### Fixed
- Cli command `update-status-traps` keeps first ocurrence and changes in type of traps

## [0.9.0] - 2025-05-01

### Added
- Add cli command `update-status-traps`

## [0.8.0] - 2024-03-13

### Added
- Add cli command `join-traps-ids-and-daily-status`

## [0.7.1] - 2024-02-27

### Changed
- Use `select_captures_from_daily_status()` inside `join_trap_info_with_captures`

### Fixed
- List of traps had duplicated elements. Remove duplicate elements.

## [0.7.0] - 2024-02-27

### Added
- Add cli command `join-captures-with-traps-info`

## [0.6.1] - 2023-09-27

### Added
- Add cli object to executable path. This way we can use it without `typer-cli` 

## [0.6.0] - 2023-07-31

### Added

- `write-monthly-summary-without-trappers()` command


[0.7.1]: https://github.com/IslasGECI/cat_data_tools/compare/v0.7.0...v0.7.1
[0.7.0]: https://github.com/IslasGECI/cat_data_tools/compare/v0.6.1...v0.7.0
[0.6.1]: https://github.com/IslasGECI/cat_data_tools/compare/v0.6.0...v0.6.1
[0.6.0]: https://github.com/IslasGECI/cat_data_tools/compare/v0.5.0...v0.6.0
