from cat_data_tools import app
from typer.testing import CliRunner


runner = CliRunner()


def test_app():
    result = runner.invoke(
        app,
        ["write-monthly-summary", "--help"],
    )
    assert "XX" not in result.stdout
    assert result.exit_code == 0
    result = runner.invoke(
        app,
        [
            "write-monthly-summary",
            "--weekly-data-path",
            "tests/data/weekly_effort_ISO.csv",
            "--monthly-trappers-path",
            "tests/data/monthly_trappers.csv",
            "--output-path",
            "tests/data/monthly_summary.csv",
        ],
    )
    assert result.exit_code == 0
