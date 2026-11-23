# Public interface

`cat-data-tools` is the command-line entry point. Run `cat-data-tools --help` to list the tasks or `cat-data-tools <task> --help` for its options. Every task reads one or more CSV files and writes one output file; a missing input path fails with a "file not found" error.

### cli write-trap-check-log --trap-daily-status-path --output-path
Rewrite a daily trap status table as the log of traps that were actually checked.

- `--trap-daily-status-path` — CSV with Spanish (`Fecha`, `Tipo`, `Estado_trampa`, `Atrayente`) or English (`Date`, `Type`, `Trap_status`, `Bait`) headers.
- `--output-path` — CSV to write.

Returns: the rows whose status starts with `R`, with English headers (`Date`, `Type`, `Trap_status`, `Bait`) and empty values written as `NA`.

Notes: `Trap_status` is replaced with the next recorded status for the same trap, and `RX` is treated as a capture (`X`).

### cli write-daily-effort-and-captures-summary-by-zone --trap-daily-status-path --output-path
Summarise daily effort and captures per zone.

- `--trap-daily-status-path` — CSV with `Fecha` or `Date`, `ID` and `Trap_status`.
- `--output-path` — CSV to write.

Returns: one row per date and zone with columns `Fecha`, `Zona`, `Esfuerzo`, `Capturas`.

Notes: effort counts the records for the day; captures count records whose status is `X`; the zone is the part of `ID` before the first `-`.

### cli write-trap-daily-status --traps-check-log-path --config-file-path --island --output-path
Rebuild the daily status of every trap from a trap check log.

- `--traps-check-log-path` — CSV with `Fecha` or `Date`, `Type`, `ID`, `Trapper`, `Trap_status` and `Bait`.
- `--config-file-path` — JSON with `days_active`, for example `{"days_active": 15}`.
- `--island` — `Socorro` or `Guadalupe`.
- `--output-path` — CSV to write.

Returns: one row per trap and day, with dates in `Fecha` and the remaining input columns preserved.

Errors: an island other than `Socorro` or `Guadalupe` raises `KeyError`.

Notes: each record is carried forward for `days_active` days. Guadalupe keeps records separate per `Trapper` because several traps share a position.

### cli write-posterior-samples-summary --posterior-results-path --effort-captures-path --output-path
Summarise the posterior samples of the population model into one JSON file.

Deprecated since 1.6.0: its functionality moves to the internals of the `eradication-stan` package.

- `--posterior-results-path` — CSV of posterior samples with `N0`, `r`, `q` and `N.*` columns.
- `--effort-captures-path` — CSV with `Fecha` and `Capturas`.
- `--output-path` — JSON to write.

Returns: a JSON object with `critical_effort`, `N0`, `r`, `q` and `time_series`; `time_series` contains `population_size`, `population_size_percentile_95`, `Date`, `Births` and `Captures`.

Notes: `critical_effort` is an integer taken from the 90th percentile of `r/q`; `N0` is the median rounded to an integer; `r` and `q` are medians. Emits a deprecation warning on every run.

### cli write-effort-captures-from-traps-and-cameras-to-json-stan --traps-effort-captures-path --cameras-effort-captures-path --output-path
Write a single Stan-ready JSON combining trap and camera effort and captures.

Deprecated since 1.6.0: its functionality moves to the internals of the `eradication-stan` package.

- `--traps-effort-captures-path` — CSV with `Fecha`, `Esfuerzo` and `Capturas`.
- `--cameras-effort-captures-path` — CSV with `Fecha`, `Esfuerzo` and `Capturas`.
- `--output-path` — JSON to write.

Returns: a JSON object with `T`, `traps_effort`, `captures`, `cameras_effort` and `detections`.

Notes: rows are matched on `Fecha` and unmatched dates are dropped; zero effort is replaced with `1`; `T` is the number of matched dates. Emits a deprecation warning on every run.

### cli write-effort-captures-as-json --effort-captures-path --output-path
Write a Stan-ready JSON from a single effort and captures table.

Deprecated since 1.6.0: its functionality moves to the internals of the `eradication-stan` package.

- `--effort-captures-path` — CSV with `Fecha`, `Esfuerzo` and `Capturas`.
- `--output-path` — JSON to write.

Returns: a JSON object with `T`, `esfuerzo` and `capturas`.

Notes: zero effort is replaced with `1`; `T` is the number of rows. Emits a deprecation warning on every run.

### cli join-traps-positions-and-active-traps-by-id-and-line --active-traps-path --traps-positions-path --output-path
Add coordinates to the traps checked during the week.

- `--active-traps-path` — CSV with `ID_de_trampa`, `line`, `date`, `Tipo_de_trampa`, `Orden` and `Estado_trampa`.
- `--traps-positions-path` — CSV with `ID`, `Linea`, `latitude` and `longitude`.
- `--output-path` — CSV to write.

Returns: columns `date`, `Tipo_de_trampa`, `ID_de_trampa`, `Orden`, `line`, `latitude` and `longitude`.

Notes: rows are matched on trap id and line (`ID_de_trampa`/`ID` and `line`/`Linea`).

### cli join-traps-ids-and-daily-status --trap-daily-status-path --traps-ids-path --output-path
Add trap identifiers and coordinates to a daily status table.

- `--trap-daily-status-path` — CSV with `ID_de_trampa` and `Estado_trampa`.
- `--traps-ids-path` — CSV with `ID`, `latitude`, `longitude` and `Linea`.
- `--output-path` — CSV to write.

Returns: the daily status rows joined with the trap table; rows with an empty `Estado_trampa` are dropped.

### cli write-monthly-summary-without-trappers --weekly-data-path --output-path
Turn weekly effort and captures into monthly totals.

- `--weekly-data-path` — CSV with `Fecha`, `Esfuerzo` and `Capturas`, or `Date`, `Effort` and `Total_individuals`.
- `--output-path` — CSV to write.

Returns: columns `Esfuerzo`, `Capturas` and `Fecha`, with `Fecha` set to the first day of the month.

### cli write-monthly-summary --weekly-data-path --monthly-trappers-path --output-path
Turn weekly effort and captures into monthly totals and add the number of trappers.

- `--weekly-data-path` — CSV with `Fecha`, `Esfuerzo` and `Capturas`.
- `--monthly-trappers-path` — CSV with `Fecha` and `Tramperos`.
- `--output-path` — CSV to write.

Returns: columns `Esfuerzo`, `Capturas`, `Fecha` and `Tramperos`, with empty values written as `NA`.

### cli filter-monthly-summary --monthly-data-path --output-path --initial-year --final-year
Deprecated since 1.3.0: use `write-filtered-monthly-summary-between-years` instead.

- `--monthly-data-path` — CSV with `Fecha` as a date.
- `--output-path` — CSV to write.
- `--initial-year` — first year to keep, default `2014`.
- `--final-year` — last year to keep, default `2019`.

Returns: the rows whose `Fecha` year is within the range, inclusive.

Notes: emits a deprecation warning on every run.

### cli write-filtered-monthly-summary-between-years --monthly-data-path --output-path --initial-year --final-year
Keep the rows of a monthly summary that fall inside a range of years.

- `--monthly-data-path` — CSV with `Fecha` as `YYYY-MM-DD`.
- `--output-path` — CSV to write.
- `--initial-year` — first year to keep, default `2014`.
- `--final-year` — last year to keep, default `2019`.

Returns: the rows whose `Fecha` year is within the range, inclusive; empty values are written as `NA`.

### cli write-filtered-data-between-dates --data-path --output-path --initial-date --final-date
Keep the rows of any table whose `Fecha` falls between two dates.

- `--data-path` — CSV with `Fecha`.
- `--output-path` — CSV to write.
- `--initial-date` — first date to keep, inclusive.
- `--final-date` — last date to keep, inclusive.

Returns: the filtered rows, unchanged.

Notes: dates are compared as `YYYY-MM-DD` values.

### cli update-status-traps --data-path --output-path
Reduce a trap history to the rows where its type or order changes.

- `--data-path` — CSV with `Tipo`, `ID`, `Orden` and `Fecha`.
- `--output-path` — CSV to write.

Returns: the first appearance of each type, id and order combination plus every row where `Tipo` or `Orden` changes, sorted by `ID` and `Fecha`; empty values are written as `NA`.

### cli version
Print the installed version of the package.

Returns: the version, for example `1.6.0`.

### transform_effort_and_captures_from_cameras_and_traps_to_dict(df_traps, df_cameras)
Python API, imported from the package root (`from cat_data_tools import transform_effort_and_captures_from_cameras_and_traps_to_dict`): build the same Stan-ready dictionary as `write-effort-captures-from-traps-and-cameras-to-json-stan`, without writing a file.

Parameters:

- `df_traps` — DataFrame with `Fecha`, `Esfuerzo` and `Capturas`.
- `df_cameras` — DataFrame with `Fecha`, `Esfuerzo` and `Capturas`.

Returns: a dictionary with `T`, `traps_effort`, `captures`, `cameras_effort` and `detections`.

Errors: `KeyError` when a required column is missing.

Notes: rows are matched on `Fecha` and unmatched dates are dropped; zero effort is replaced with `1`; `T` is the number of matched dates.

### transform_effort_captures_to_dict(df, effort="esfuerzo", captures="capturas")
Python API, imported from the package root (`from cat_data_tools import transform_effort_captures_to_dict`): build the same Stan-ready dictionary as `write-effort-captures-as-json`, without writing a file.

Parameters:

- `df` — DataFrame with `Fecha`, `Esfuerzo` and `Capturas`.
- `effort` — key name for the effort values in the returned dictionary, default `esfuerzo`.
- `captures` — key name for the captures values in the returned dictionary, default `capturas`.

Returns: a dictionary with `T` and the effort and captures lists under the names given by `effort` and `captures`.

Notes: zero effort is replaced with `1`; `T` is the number of rows; the input DataFrame is not modified.

### compute_posterior_summary_for_cameras_and_traps(posterior_samples, traps_effort_and_captures_df, cameras_effort_and_captures_df)
Python API, imported from the package root (`from cat_data_tools import compute_posterior_summary_for_cameras_and_traps`): summarise the posterior samples of the traps-and-cameras model.

Parameters:

- `posterior_samples` — DataFrame with `N0`, `r`, `traps_q`, `cameras_q` and `N.*` columns.
- `traps_effort_and_captures_df` — DataFrame with `Fecha` and `Capturas`.
- `cameras_effort_and_captures_df` — DataFrame with `Capturas`.

Returns: a dictionary with `critical_effort`, `N0`, `r`, `traps_q`, `cameras_q` and `time_series`.

Notes: `critical_effort` is the 90th percentile of `r / traps_q` rounded to an integer; `N0` is the median rounded to an integer; `r`, `traps_q` and `cameras_q` are medians; `time_series` contains `population_size`, `population_size_percentile_95`, `Date`, `Births`, `Captures` and `Detections`.

### compute_posterior_summary_for_traps(posterior_samples, traps_effort_and_captures_df)
Python API, imported from the package root (`from cat_data_tools import compute_posterior_summary_for_traps`): summarise the posterior samples of the traps-only model.

Parameters:

- `posterior_samples` — DataFrame with `N0`, `r`, `traps_q` and `N.*` columns.
- `traps_effort_and_captures_df` — DataFrame with `Fecha` and `Capturas`.

Returns: a dictionary with `critical_effort`, `N0`, `r`, `traps_q` and `time_series`.

Notes: `critical_effort` is the 90th percentile of `r / traps_q` rounded to an integer; `N0` is the median rounded to an integer; `r` and `traps_q` are medians; `time_series` contains `population_size`, `population_size_percentile_95`, `Date`, `Births` and `Captures`, without `Detections`.
