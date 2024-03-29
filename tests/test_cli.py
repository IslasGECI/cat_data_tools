from cat_data_tools.cli import app
from typer.testing import CliRunner
import os
import pandas as pd


runner = CliRunner()


def test_app_join_traps_ids_and_daily_status():
    command = "join-traps-ids-and-daily-status"
    assert_cli_help(command)
    output_path = "tests/data/traps_and_daily_status_for_looker.csv"

    if os.path.exists(output_path):
        os.remove(output_path)

    result = runner.invoke(
        app,
        [
            command,
            "--trap-daily-status-path",
            "tests/data/daily_status_trap_guadalupe.csv",
            "--traps-ids-path",
            "tests/data/traps_ids_latlon.csv",
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    obtained = pd.read_csv(output_path)
    assert len(obtained.columns) == 6
    os.remove(output_path)


def test_app_join_captures_with_traps_info():
    command = "join-captures-with-traps-info"
    assert_cli_help(command)
    output_path = "tests/data/joined_traps_with_captures.csv"

    if os.path.exists(output_path):
        os.remove(output_path)

    result = runner.invoke(
        app,
        [
            command,
            "--trap-daily-status-path",
            "tests/data/trap_daily_status.csv",
            "--traps-info-path",
            "tests/data/traps_list.csv",
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    assert os.path.exists(output_path)
    obtained = pd.read_csv(output_path)
    expected_n_columns = 5
    obtained_n_columns = len(obtained.columns)
    assert obtained_n_columns == expected_n_columns


def test_app_write_monthly_summary():
    result = runner.invoke(
        app,
        ["version"],
    )
    assert "0.8.0" in result.stdout
    assert result.exit_code == 0

    command = "write-monthly-summary"
    assert_cli_help(command)

    output_path = "tests/data/monthly_summary.csv"
    result = runner.invoke(
        app,
        [
            "write-monthly-summary",
            "--weekly-data-path",
            "tests/data/weekly_effort_ISO.csv",
            "--monthly-trappers-path",
            "tests/data/monthly_trappers.csv",
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    os.remove(output_path)


def test_app_write_monthly_summary_without_trappers():
    command = "write-monthly-summary-without-trappers"
    result = assert_cli_help(command)
    assert "XXXX" not in result.stdout

    output_path = "tests/data/monthly_summary.csv"
    result = runner.invoke(
        app,
        [
            "write-monthly-summary-without-trappers",
            "--weekly-data-path",
            "tests/data/weekly_effort_ISO.csv",
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    os.remove(output_path)


def test_app_filter_monthly_summary():
    command = "filter-monthly-summary"
    result = assert_cli_help(command)
    assert "XXXX" not in result.stdout
    assert "[default: 2014]" in result.stdout
    assert "[default: 2019]" in result.stdout

    output_path = "tests/data/yearly_summary.csv"
    result = runner.invoke(
        app,
        [
            "filter-monthly-summary",
            "--monthly-data-path",
            "tests/data/esfuerzo_capturas_mensuales_gatos_socorro_3_years.csv",
            "--initial-year",
            2015,
            "--final-year",
            2018,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    os.remove(output_path)


def assert_cli_help(command):
    result = runner.invoke(
        app,
        [command, "--help"],
    )
    assert "XX" not in result.stdout
    assert result.exit_code == 0
    return result
