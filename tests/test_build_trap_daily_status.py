from cat_data_tools.build_trap_daily_status import xxbuild_trap_daily_status
import pandas as pd


def tests_build_trap_daily_status():

    check_traps_log_df = pd.read_csv("tests/data/check_traps_log.csv")
    active_days = 7
    obtained = xxbuild_trap_daily_status(check_traps_log_df, active_days)
    assert isinstance(obtained, pd.DataFrame)
    expected_days_for_trap_001 = 14
    assert len(obtained[obtained["ID"] == "10-001"]) == expected_days_for_trap_001
    expected_days_for_trap_002 = 11
    assert len(obtained[obtained["ID"] == "10-002"]) == expected_days_for_trap_002
    expected_days_for_trap_003 = 5
    assert len(obtained[obtained["ID"] == "10-003"]) == expected_days_for_trap_003
    expected_days_for_trap_004 = 10
    assert len(obtained[obtained["ID"] == "10-004"]) == expected_days_for_trap_004
