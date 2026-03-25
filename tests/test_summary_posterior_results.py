from cat_data_tools.summary_posterior_results import compute_critical_effort, compute_N0
import pandas as pd

posterior_samples = pd.read_csv("tests/data/posterior_results.csv")


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
