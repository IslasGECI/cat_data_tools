# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Fixed

### Changed

### Removed

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
