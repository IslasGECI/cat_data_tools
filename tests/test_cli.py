from cat_data_tools.cli import app
from typer.testing import CliRunner
import os


runner = CliRunner()


def test_app():
    result = runner.invoke(
        app,
        ["version"],
    )
    assert "0.4.1" in result.stdout
    assert result.exit_code == 0

    result = runner.invoke(
        app,
        ["write-monthly-summary", "--help"],
    )
    assert "XX" not in result.stdout
    assert result.exit_code == 0
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
    output_path = "tests/data/yearly_summary.csv"
    result = runner.invoke(
        app,
        [
            "write-yearly-summary",
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
    # os.remove(output_path)
