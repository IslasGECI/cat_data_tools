from cat_data_tools.summary_posterior_results import compute_critical_effort
import pandas as pd


def test_compute_critical_effort():
    posterior_samples = pd.read_csv("tests/data/posterior_results.csv")
    obtained = compute_critical_effort(posterior_samples)
    assert isinstance(obtained, float)
