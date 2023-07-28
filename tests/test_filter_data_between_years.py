from cat_data_tools import (
    filter_data_after_year,
    filter_data_before_year,
    filter_data_between_years,
)

import pandas as pd


monthly_data = pd.read_csv("tests/data/esfuerzo_capturas_mensuales_gatos_socorro_3_years.csv")
year = 2016
expected = pd.read_csv("tests/data/filtered_data_after_2016.csv")


def test_filter_data_after_year():
    obtained = filter_data_after_year(monthly_data, year)
    obtained_length = len(obtained)

    expected = pd.read_csv("tests/data/filtered_data_after_2016.csv")
    expected_length = len(expected)
    assert obtained_length == expected_length


def test_filter_data_before_year():
    year = 2017
    obtained = filter_data_before_year(monthly_data, year)
    expected = pd.read_csv("tests/data/filtered_data_before_2017.csv")
    obtained_length = len(obtained)
    expected_length = len(expected)
    assert obtained_length == expected_length


def test_filter_data_between_years():
    initial_year = 2016
    final_year = 2017
    obtained = filter_data_between_years(monthly_data, initial_year, final_year).reset_index(
        drop=True
    )
    obtained["Fecha"] = obtained["Fecha"].dt.strftime("%Y-%m-%d")
    expected = pd.read_csv("tests/data/filtered_data_between_2016_and_2017.csv")
    pd.testing.assert_frame_equal(obtained, expected)

    obtained = filter_data_between_years(monthly_data, initial_year)
    obtained_length = len(obtained)
    expected = pd.read_csv("tests/data/filtered_data_between_years_2016_and_2260.csv")
    expected_length = len(expected)
    assert obtained_length == expected_length
