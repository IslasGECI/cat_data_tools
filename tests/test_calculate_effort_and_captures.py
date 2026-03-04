from cat_data_tools.calculate_effort_and_captures import calculate_effort_and_captures

import pandas as pd


def test_calculate_effort_and_captures():
    daily_status = pd.read_csv("tests/data/reconstructed_daily_status.csv")
    obtained = calculate_effort_and_captures(daily_status)
    expected_rows = 11
    assert len(obtained) == expected_rows
    expected_effort_zone_01 = 2
    assert obtained[obtained["Zone"] == "01"].Effort.iloc[0] == expected_effort_zone_01
    expected_captures_zone_01 = 1
    mask = (obtained["Zone"] == "01") & (obtained["Date"] == "2023-04-07")
    assert obtained[mask].Captures.values[0] == expected_captures_zone_01
