from cat_data_tools import join_trap_ids_and_daily_status

import pandas as pd


def test_join_trap_ids_and_daily_status():
    trap_daily_status = pd.read_csv("tests/data/trap_daily_status.csv")
    trap_ids = pd.read_csv("tests/data/traps_ids_latlon.csv")
    join_trap_ids_and_daily_status(trap_daily_status, trap_ids)
