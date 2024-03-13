from cat_data_tools import join_trap_ids_and_daily_status

import pandas as pd


def test_join_trap_ids_and_daily_status():
    trap_daily_status = pd.read_csv("tests/data/daily_status_trap_guadalupe.csv")
    trap_ids = pd.read_csv("tests/data/traps_ids_latlon.csv")
    obtained = join_trap_ids_and_daily_status(trap_daily_status, trap_ids)
    assert len(obtained) == len(trap_daily_status) - 1
    assert len(obtained.columns) == 6
