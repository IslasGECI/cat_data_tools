from cat_data_tools.detect_status_change import (
    add_next_status_column,
    get_status_change,
    subsitute_check_traps_status,
)

import pandas as pd
import numpy as np


def tests_get_status_change():
    daily_status_df = pd.read_csv("tests/data/daily_status_two_traps.csv")
    obtained = get_status_change(daily_status_df)
    expected_status_changes = 22
    assert len(obtained) == expected_status_changes


def test_add_next_status_column():
    daily_status_df = pd.read_csv("tests/data/daily_status_with_r_in_check.csv")
    obtained = add_next_status_column(daily_status_df)
    assert obtained.loc[0, "next_status"] == "A"


def test_subsitute_check_traps_status():
    df = pd.DataFrame(
        {
            "ID": ["01-001", "01-001", "01-002", "01-002"],
            "Trap_status": ["RD", "A", "RD", "D"],
            "next_status": ["A", np.nan, "D", np.nan],
        }
    )
    obtained = subsitute_check_traps_status(df)
    assert obtained.loc[0, "Trap_status"] == "A"
