from cat_data_tools.summary_posterior_results import (
    compute_birth_rate,
    compute_catchability,
    compute_critical_effort,
    compute_N0,
    compute_population_size_time_series,
    compute_posterior_summary,
)
import pandas as pd
import pytest

posterior_samples = pd.read_csv("tests/data/posterior_results.csv")


effort_captures_df = pd.read_csv("tests/data/monthly_effort_captures_for_tests.csv")


expected_time_series_keys = [
    "population_size",
    "Date",
    "Births",
    "Captures",
    "population_size_percentile_95",
]


def test_compute_posterior_summary():
    obtained = compute_posterior_summary(posterior_samples, effort_captures_df)
    expected_keys = ["critical_effort", "r", "q", "N0", "time_series"]
    assert set(obtained.keys()) == set(expected_keys)
    assert set(obtained["time_series"].keys()) == set(expected_time_series_keys)


def test_compute_population_size_time_series():
    expected_series_length = 35
    obtained = compute_population_size_time_series(posterior_samples, effort_captures_df)
    assert len(obtained["population_size"]) == expected_series_length
    assert len(obtained["Date"]) == expected_series_length
    assert isinstance(obtained["population_size"], list)
    assert all(
        [
            row1 < row2
            for row1, row2 in zip(
                obtained["population_size"], obtained["population_size_percentile_95"]
            )
        ]
    )


def test_compute_critical_effort():
    obtained = compute_critical_effort(posterior_samples)
    assert isinstance(obtained, int)
    expected_critical_effort = 10185
    assert obtained == expected_critical_effort


def tests_compute_N0():
    obtained = compute_N0(posterior_samples)
    assert isinstance(obtained, int)
    expected_N0 = 72
    assert obtained == expected_N0


def test_compute_birth_rate():
    obtained = compute_birth_rate(posterior_samples)
    assert isinstance(obtained, float)
    expected_r = 0.27993238
    assert pytest.approx(obtained, rel=0.05) == expected_r


def test_compute_catchability():
    obtained = compute_catchability(posterior_samples)
    assert isinstance(obtained, float)
    expected_q = 2.8105986e-05
    assert pytest.approx(obtained, rel=0.05) == expected_q
