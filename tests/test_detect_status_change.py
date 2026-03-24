from cat_data_tools.detect_status_change import (
    add_next_status_column,
    compute_trap_check_log,
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


def test_compute_trap_check_log():
    daily_status_df = pd.read_csv("tests/data/daily_status_with_r_in_check.csv")
    obtained = compute_trap_check_log(daily_status_df)
    expected_colums = [
        "Date",
        "Type",
        "ID",
        "Trapper",
        "Trap_status",
        "Bait",
        "Nombre_del_responsable",
    ]
    assert obtained.colums == expected_colums


def test_add_next_status_column():
    daily_status_df = pd.read_csv("tests/data/daily_status_with_r_in_check.csv")
    obtained = add_next_status_column(daily_status_df)
    assert obtained.loc[0, "next_status"] == "A"
    mask = (obtained["Date"] == "2026-03-05") & (obtained["ID"] == "03-191")
    assert obtained[mask]["next_status"].values[0] == "X"


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
    expected_rows = 2
    assert len(obtained) == expected_rows
