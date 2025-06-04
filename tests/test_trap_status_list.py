from cat_data_tools.trap_status_list import (
    join_trap_ids_and_daily_status,
    add_lat_lon_to_active_traps_of_the_week,
)

import pandas as pd


def test_join_trap_ids_and_daily_status():
    trap_daily_status = pd.read_csv("tests/data/daily_status_trap_guadalupe.csv")
    trap_ids = pd.read_csv("tests/data/traps_ids_latlon.csv")
    obtained = join_trap_ids_and_daily_status(trap_daily_status, trap_ids)
    assert len(obtained) == len(trap_daily_status) - 1
    assert len(obtained.columns) == 6


def tests_add_lat_lon_to_active_traps_of_the_week():
    active_traps = pd.read_csv("tests/data/active_traps_splitted.csv")
    traps_positions_with_lat_lon = pd.read_csv("tests/data/traps_positions_with_latlon.csv")
    obtained = add_lat_lon_to_active_traps_of_the_week(active_traps, traps_positions_with_lat_lon)
