import pandas as pd

import click
from click_default_group import DefaultGroup


@click.group(cls=DefaultGroup, default="create", default_if_no_args=True)
def cli():
    pass


@cli.command(short_help="Filter data from Socorro Island Eradication Project")
@click.option("--weekly-data-path", "-d", type=click.Path(), help="Path to the weekly data")
@click.option(
    "--monthly-trappers-path",
    "-t",
    type=click.Path(),
    help="Path to the monthly number of trappers",
)
@click.option("--output-path", "-o", type=click.Path(), help="Output file path")
def write_monthly_summary(weekly_data_path: str, monthly_trappers_path: str, output_path: str):
    effort_data = pd.read_csv(weekly_data_path)
    monthly_trappers = pd.read_csv(monthly_trappers_path)
    monthly_data = summarize_effort_captures_and_trappers(monthly_trappers, effort_data)
    monthly_data.to_csv(output_path, index=False, na_rep="NA")


def summarize_effort_captures_and_trappers(monthly_trappers, effort_data):
    monthly_data = sum_monthly_effort_and_captures(effort_data)
    monthly_data = add_date_column(monthly_data)
    monthly_data["Tramperos"] = monthly_trappers["Tramperos"]
    monthly_data = monthly_data.drop(columns=["month_and_year", "Zona"])
    return monthly_data


def add_date_column(monthly_data):
    monthly_data.reset_index(inplace=True)
    monthly_data = monthly_data.rename(columns={"index": "month_and_year"})
    monthly_data["Fecha"] = monthly_data.month_and_year + "-01"
    return monthly_data


def sum_monthly_effort_and_captures(effort_data: pd.DataFrame):
    effort_data["month_and_year"] = effort_data.Fecha.str[:7]
    monthly_grouped_data = effort_data.groupby(by="month_and_year", sort=False)
    return monthly_grouped_data.sum(numeric_only=True)
