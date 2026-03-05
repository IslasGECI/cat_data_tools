from cat_data_tools.cli import app
import geci_test_tools as gtt
from typer.testing import CliRunner
import os
import pandas as pd

runner = CliRunner()


def test_write_daily_effort_and_captures_summary_by_zone():
    command = "write-daily-effort-and-captures-summary-by-zone"
    assert_cli_help(command)

    output_path = "tests/traps_effort_captures_daily_summary.csv"
    gtt.if_exist_remove(output_path)

    trap_daily_status_path = "tests/data/daily_status_two_traps.csv"
    result = runner.invoke(
        app,
        [
            command,
            "--trap-daily-status-path",
            trap_daily_status_path,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    gtt.assert_exist(output_path)
    expected_headers = ["Fecha", "Zona", "Esfuerzo", "Capturas"]
    obtained = pd.read_csv(output_path)
    assert list(obtained.columns) == expected_headers
    gtt.if_exist_remove(output_path)


def test_write_trap_daily_status():
    command = "write-trap-daily-status"
    assert_cli_help(command)

    output_path = "tests/trap_daily_status.csv"
    gtt.if_exist_remove(output_path)

    traps_check_log_path = "tests/data/check_traps_log.csv"
    trap_daily_status_config_path = "tests/data/trap_daily_status_config.json"
    result = runner.invoke(
        app,
        [
            command,
            "--traps-check-log-path",
            traps_check_log_path,
            "--config-file-path",
            trap_daily_status_config_path,
            "--island",
            "Socorro",
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    gtt.assert_exist(output_path)
    expected_headers = ["Fecha", "Type", "ID", "Trapper", "Trap_status", "Bait"]
    obtained = pd.read_csv(output_path)
    assert list(obtained.columns) == expected_headers
    os.remove(output_path)
    spanish_date_df = pd.read_csv(traps_check_log_path)
    spanish_date_df.rename(columns={"Date": "Fecha"}, inplace=True)
    spanish_traps_check_log_path = "tests/data/check_traps_log_spanish_dates.csv"
    spanish_date_df.to_csv(spanish_traps_check_log_path, index=False)

    result = runner.invoke(
        app,
        [
            command,
            "--traps-check-log-path",
            spanish_traps_check_log_path,
            "--config-file-path",
            trap_daily_status_config_path,
            "--island",
            "Guadalupe",
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    gtt.assert_exist(output_path)
    obtained = pd.read_csv(output_path)
    expected_rows = 161
    assert len(obtained) == expected_rows
    gtt.if_exist_remove(spanish_traps_check_log_path)
    gtt.if_exist_remove(output_path)


def test_write_effort_captures_as_json():
    command = "write-effort-captures-as-json"
    assert_cli_help(command)

    output_path = "tests/effort_captures.json"
    gtt.if_exist_remove(output_path)

    effort_captures_path = "tests/data/esfuerzo_capturas_mensuales_gatos_socorro_3_years.csv"
    result = runner.invoke(
        app,
        [
            command,
            "--effort-captures-path",
            effort_captures_path,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    gtt.assert_exist(output_path)
    os.remove(output_path)


def test_app_join_traps_positions_and_active_traps_by_id_and_line():
    command = "join-traps-positions-and-active-traps-by-id-and-line"
    assert_cli_help(command)
    output_path = "tests/data/traps_check_this_week.csv"

    gtt.if_exist_remove(output_path)

    result = runner.invoke(
        app,
        [
            command,
            "--active-traps-path",
            "tests/data/active_traps_splitted.csv",
            "--traps-positions-path",
            "tests/data/traps_positions_with_latlon.csv",
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    gtt.assert_exist(output_path)
    os.remove(output_path)


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


def test_app_write_monthly_summary():
    result = runner.invoke(
        app,
        ["version"],
    )
    assert "1.0.0" in result.stdout
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


def test_update_status_traps():
    command = "update-status-traps"
    result = assert_cli_help(command)

    output_path = "tests/data/traps_info_updated.csv"
    gtt.if_exist_remove(output_path)
    result = runner.invoke(
        app,
        [
            "update-status-traps",
            "--data-path",
            "tests/data/traps_info_for_tests.csv",
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    gtt.assert_exist(output_path)


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
