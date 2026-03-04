from cat_data_tools.calculate_effort_and_captures import calculate_effort_and_captures

import pandas as pd


def test_calculate_effort_and_captures():
    daily_status = pd.read_csv("tests/data/reconstructed_daily_status.csv")
    obtained = calculate_effort_and_captures(daily_status)
    expected_rows = 11
    assert len(obtained) == expected_rows
