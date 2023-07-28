import pandas as pd
import click
from click_default_group import DefaultGroup


@click.group(cls=DefaultGroup, default="create", default_if_no_args=True)
def cli():
    pass


@cli.command(short_help="Filter data from Socorro Island Eradication Project")
@click.option("--input-path", "-r", type=click.Path(), help="Input file path")
@click.option("--output-path", "-w", type=click.Path(), help="Output file path")
@click.option("--initial-year", "-i", type=int, help="Initial year")
@click.option("--final-year", "-f", default=3000, type=int, help="Final year")
def write_filtered_data(input_path, output_path, initial_year, final_year):
    dataframe = pd.read_csv(input_path)
    filtered_dataframe = filter_data_between_years(dataframe, initial_year, final_year)
    filtered_dataframe.to_csv(output_path, index=False, na_rep="NA")


def filter_data_between_years(monthly_data, initial_year, final_year=3000):
    data_after_year = filter_data_after_year(monthly_data, initial_year)
    return filter_data_before_year(data_after_year, final_year)


def filter_data_after_year(monthly_data, year):
    monthly_data_copy = str_2_datetime(monthly_data)
    return monthly_data_copy[monthly_data_copy.Fecha.dt.year >= year]


def filter_data_before_year(monthly_data, year):
    monthly_data_copy = str_2_datetime(monthly_data)
    return monthly_data_copy[monthly_data_copy.Fecha.dt.year <= year]


def str_2_datetime(monthly_data):
    monthly_data_copy = monthly_data.copy()
    monthly_data_copy["Fecha"] = pd.to_datetime(monthly_data_copy.Fecha, format="%Y-%m-%d")
    return monthly_data_copy
