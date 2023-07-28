from cat_data_tools import (
    sum_monthly_effort_and_captures,
    summarize_effort_captures_and_trappers,
    write_monthly_summary,
)
import pandas as pd
import numpy as np
import subprocess
import os


weekly_data_path = "tests/data/weekly_effort_ISO.csv"
monthly_trappers_path = "tests/data/monthly_trappers.csv"


def test_sum_monthly_effort_and_captures():
    effort_data = pd.read_csv(weekly_data_path)
    filtered_data = sum_monthly_effort_and_captures(effort_data)
    expected_rows = 7
    obtained_rows = len(filtered_data)
    assert obtained_rows == expected_rows
    obtained_captures = filtered_data.loc["2022-04", "Capturas"]
    expected_captures = 0
    assert obtained_captures == expected_captures
    obtained_captures = filtered_data.loc["2023-03", "Capturas"]
    expected_captures = 2
    assert obtained_captures == expected_captures


def test_summarize_effort_captures_and_trappers():
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


def test_write_monthly_summary():
    output_path = "tests/data/monthly_summary.csv"
    write_monthly_summary(weekly_data_path, monthly_trappers_path, output_path)
    obtained = str(subprocess.check_output([f"cat {output_path}"], shell=True))
    assert ",NA" in obtained
    assert ",Esfuerzo" not in obtained
    os.remove(output_path)
