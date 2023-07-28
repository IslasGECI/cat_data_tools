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
