from cat_data_tools import select_captures_from_daily_status
import pandas as pd


def test_select_captures_from_daily_status():
    daily_status = pd.read_csv("tests/data/trap_daily_status.csv")
    obtained = select_captures_from_daily_status(daily_status)
    expected_captures = 2
    assert len(obtained) == expected_captures
