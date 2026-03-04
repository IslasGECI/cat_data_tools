from cat_data_tools.detect_status_change import get_status_change

import pandas as pd


def tests_get_status_change():
    daily_status_df = pd.read_csv("tests/data/daily_status_one_trap.csv")
    obtained = get_status_change(daily_status_df)
    expected_status_changes = 18
    assert len(obtained) == expected_status_changes
