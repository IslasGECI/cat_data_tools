from gatos_socorro import sum_monthly_effort_and_captures, summarize_effort_captures_and_trappers
import pandas as pd
import numpy as np

weekly_data_path = "tests/data/weekly_effort_ISO.csv"


def test_sum_monthly_effort_and_captures():
    effort_data = pd.read_csv(weekly_data_path)
    filtered_data = sum_monthly_effort_and_captures(effort_data)
    print(filtered_data)
    expected_rows = 7
    obtained_rows = len(filtered_data)
    assert obtained_rows == expected_rows
    obtained_captures = filtered_data.loc["2022-04", "Capturas"]
    expected_captures = 0
    assert obtained_captures == expected_captures
    obtained_captures = filtered_data.loc["2023-03", "Capturas"]
    expected_captures = 2
    assert obtained_captures == expected_captures


def test_write_monthly_summary():
    monthly_trappers_path = "tests/data/monthly_trappers.csv"
    monthly_trappers = pd.read_csv(monthly_trappers_path)
    effort_data = pd.read_csv(weekly_data_path)
    obtained_data = summarize_effort_captures_and_trappers(monthly_trappers, effort_data)
    obtained_columns = obtained_data.columns
    expected_columns = ["Esfuerzo", "Capturas", "Fecha", "Tramperos"]
    assert (obtained_columns == expected_columns).all()
    obtained_date = obtained_data.loc[0, "Fecha"]
    expected_date = "2021-12-01"
    assert obtained_date == expected_date
    obtained_trappers = obtained_data.loc[:, "Tramperos"]
    expected_trappers = pd.Series([15, 2, np.nan, 4, 1, 18, 7])
    pd.testing.assert_series_equal(obtained_trappers, expected_trappers, check_names=False)
