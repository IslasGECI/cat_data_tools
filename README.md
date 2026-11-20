# Cat data tools <a href="https://www.islas.org.mx/"><img src="https://www.islas.org.mx/img/logo.svg" align="right" width="256" /></a>

[![codecov](https://codecov.io/gh/IslasGECI/cat_data_tools/branch/develop/graph/badge.svg?token=MvLBzyGSH3)](https://codecov.io/gh/IslasGECI/cat_data_tools)
![licencia](https://img.shields.io/github/license/IslasGECI/cat_data_tools)
![languages](https://img.shields.io/github/languages/top/IslasGECI/cat_data_tools)
![commits](https://img.shields.io/github/commit-activity/y/IslasGECI/cat_data_tools)
![GitHub contributors](https://img.shields.io/github/contributors/IslasGECI/cat_data_tools)

Turn the field records of cat-trapping and camera campaigns into tidy summaries of effort, captures and population size.

## What it does

- Rebuilds the daily status of every trap from the field check logs.
- Summarises effort and captures by day and zone, and turns weekly records into monthly totals, with or without the number of trappers.
- Filters summaries by year or by a range of dates.
- Keeps the trap master list (type and order) consistent over time.
- Adds latitude and longitude to the traps checked each week, so captures can be mapped.
- Prepares the numbers the population model needs as a JSON file, ready to run.

## Usage

Run `cat-data-tools --help` to list every task, or `cat-data-tools <task> --help` to see what a task needs.

For example, to build a monthly summary that includes the number of trappers:

    cat-data-tools write-monthly-summary \
        --weekly-data-path weekly.csv \
        --monthly-trappers-path trappers.csv \
        --output-path monthly.csv

Every task reads one or more CSV files and writes a single output file. Dates go in a column called `Fecha`, and effort and captures are expected as `Esfuerzo` and `Capturas`. A few tasks also accept English headers (`Date`, `Effort`, `Total_individuals`), as their help explains.

## Before you start

- The CSV tables you want to process. No database, account or key is needed.
- Docker (recommended) or Python 3.9 or newer.

## Run the project

### With Docker (recommended)

    docker build --tag islasgeci/cat_data_tools:latest .
    docker compose run --rm islasgeci

The project folder is mounted at `/workdir`, and `cat-data-tools` is ready to use inside the container.

### With Python

    pip install --editable .
    cat-data-tools --help
