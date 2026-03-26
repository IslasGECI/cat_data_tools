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


def test_compute_posterior_summary():
    obtained = compute_posterior_summary(posterior_samples)
    expected_keys = ["critical_effort", "r", "q", "N0"]
    assert set(obtained.keys()) == set(expected_keys)


def test_compute_population_size_time_series():
    obtained = compute_population_size_time_series(posterior_samples)
    expected_keys = ["population_size", "Date"]
    assert set(obtained.keys()) == set(expected_keys)
    expected_series_length = 35
    assert len(obtained["population_size"]) == expected_series_length


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
