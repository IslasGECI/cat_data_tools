from cat_data_tools.build_trap_daily_status import build_trap_daily_status
import pandas as pd


def tests_build_trap_daily_status():

    check_traps_log_df = pd.read_csv("tests/data/check_traps_log.csv")
    obtained = build_trap_daily_status(check_traps_log_df)
    assert isinstance(obtained, pd.DataFrame)
