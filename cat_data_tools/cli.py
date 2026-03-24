from cat_data_tools.filter_data_by_month import (
    summarize_effort_captures_and_add_trappers,
    summarize_effort_captures,
)
from cat_data_tools.build_trap_daily_status import (
    _build_trap_daily_status,
    _build_trap_daily_status_for_duplicated_positions,
)
from cat_data_tools.calculate_effort_and_captures import calculate_effort_and_captures
from cat_data_tools.detect_status_change import (
    add_next_status_column,
    compute_trap_check_log,
    subsitute_check_traps_status,
)
from cat_data_tools.filter_data_between_years import filter_data_between_years
from cat_data_tools.update_status_traps import _update_status_traps
from cat_data_tools.transform_effort_captures import transform_effort_captures_to_dict
import cat_data_tools as cdt
import pandas as pd
import json
import typer

app = typer.Typer()


@app.command()
def write_trap_check_log(
    trap_daily_status_path: str = typer.Option(),
    output_path: str = typer.Option(),
):
    daily_status_df = pd.read_csv(trap_daily_status_path)
    daily_status_df_renamed = daily_status_df.rename(
        columns={
            "Fecha": "Date",
            "Tipo": "Type",
            "Estado_trampa": "Trap_status",
            "Atrayente": "Bait",
        }
    )
    check_log = compute_trap_check_log(daily_status_df_renamed)
    check_log.to_csv(output_path, index=False)


@app.command()
def write_daily_effort_and_captures_summary_by_zone(
    trap_daily_status_path: str = typer.Option(),
    output_path: str = typer.Option(),
):
    trap_daily_status_df = adapt_date_column_name(trap_daily_status_path)
    effort_captures_summary_df = calculate_effort_and_captures(trap_daily_status_df)
    effort_captures_summary_df_renamed = effort_captures_summary_df.rename(
        columns={"Date": "Fecha", "Zone": "Zona", "Effort": "Esfuerzo", "Captures": "Capturas"}
    )
    effort_captures_summary_df_renamed.to_csv(output_path, index=False)


@app.command()
def write_trap_daily_status(
    traps_check_log_path: str = typer.Option(),
    config_file_path: str = typer.Option(),
    island: str = typer.Option(),
    output_path: str = typer.Option(),
):
    traps_check_log_df = adapt_date_column_name(traps_check_log_path)

    with open(config_file_path, "r") as file:
        config = json.load(file)
    build_methods = {
        "Guadalupe": _build_trap_daily_status_for_duplicated_positions,
        "Socorro": _build_trap_daily_status,
    }
    trap_daily_status_df = build_methods[island](
        traps_check_log_df, days_active=config["days_active"]
    )
    trap_daily_status_df_renamed = trap_daily_status_df.rename(columns={"Date": "Fecha"})
    trap_daily_status_df_renamed.to_csv(output_path, index=False)


def adapt_date_column_name(input_path):
    input_df = pd.read_csv(input_path)
    return input_df.rename(columns={"Fecha": "Date"})


@app.command()
def write_effort_captures_as_json(
    effort_captures_path: str = typer.Option(), output_path: str = typer.Option()
):
    effort_captures_df = pd.read_csv(effort_captures_path)
    effort_captures_dict = transform_effort_captures_to_dict(effort_captures_df)
    write_dict_as_json(effort_captures_dict, output_path)


def write_dict_as_json(data_dict, output_path):
    json_string = json.dumps(data_dict, indent=2)
    with open(output_path, "w") as json_file:
        json_file.write(json_string)


@app.command()
def join_traps_positions_and_active_traps_by_id_and_line(
    active_traps_path: str = "", traps_positions_path: str = "", output_path: str = ""
):
    active_traps = pd.read_csv(active_traps_path)
    postions_with_lat_lon = pd.read_csv(traps_positions_path)
    joined_df = cdt.add_lat_lon_to_active_traps_of_the_week(active_traps, postions_with_lat_lon)
    joined_df.to_csv(output_path, index=False)


@app.command()
def join_traps_ids_and_daily_status(
    trap_daily_status_path: str = "", traps_ids_path: str = "", output_path: str = ""
):
    trap_daily_status = pd.read_csv(trap_daily_status_path)
    traps_ids = pd.read_csv(traps_ids_path)
    joined_df = cdt.join_trap_ids_and_daily_status(trap_daily_status, traps_ids)
    joined_df.to_csv(output_path, index=False)


@app.command(help="Write monthly summary from weekly summary without trappers")
def write_monthly_summary_without_trappers(weekly_data_path: str = "", output_path: str = ""):
    effort_data = pd.read_csv(weekly_data_path)
    monthly_data = summarize_effort_captures(effort_data)
    monthly_data.to_csv(output_path, index=False)


@app.command(help="Write monthly summary from weekly summary")
def write_monthly_summary(
    weekly_data_path: str = "", monthly_trappers_path: str = "", output_path: str = ""
):
    effort_data = pd.read_csv(weekly_data_path)
    monthly_trappers = pd.read_csv(monthly_trappers_path)
    monthly_data = summarize_effort_captures_and_add_trappers(monthly_trappers, effort_data)
    monthly_data.to_csv(output_path, index=False, na_rep="NA")


@app.command(help="Filter monthly summary between years")
def filter_monthly_summary(
    monthly_data_path: str = "",
    output_path: str = "",
    initial_year: int = 2014,
    final_year: int = 2019,
):
    dataframe = pd.read_csv(monthly_data_path)
    filtered_dataframe = filter_data_between_years(dataframe, initial_year, final_year)
    filtered_dataframe.to_csv(output_path, index=False, na_rep="NA")


@app.command()
def update_status_traps(data_path: str = typer.Option(), output_path: str = typer.Option()):
    traps_info_df = pd.read_csv(data_path)
    updated_traps_info = _update_status_traps(traps_info_df)
    updated_traps_info.to_csv(output_path, index=False, na_rep="NA")


@app.command()
def version():
    print(cdt.__version__)
