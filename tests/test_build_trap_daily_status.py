from cat_data_tools.build_trap_daily_status import (
    build_trap_daily_status,
    build_trap_daily_status_for_duplicated_positions,
)
import pandas as pd

active_days = 7


def tests_build_trap_daily_status():
    check_traps_log_df = pd.read_csv("tests/data/check_traps_log.csv")
    obtained = build_trap_daily_status(check_traps_log_df, active_days)
    obtained.to_csv("salida.csv", index=False)
    assert isinstance(obtained, pd.DataFrame)
    expected_days_for_trap_001 = 14
    assert len(obtained[obtained["ID"] == "10-001"]) == expected_days_for_trap_001
    expected_days_for_trap_002 = 11
    assert len(obtained[obtained["ID"] == "10-002"]) == expected_days_for_trap_002
    expected_days_for_trap_003 = 5
    assert len(obtained[obtained["ID"] == "10-003"]) == expected_days_for_trap_003
    expected_days_for_trap_004 = 10
    assert len(obtained[obtained["ID"] == "10-004"]) == expected_days_for_trap_004
    expected_days_for_trap_005 = 12
    assert len(obtained[obtained["ID"] == "10-005"]) == expected_days_for_trap_005
    expected_days_for_trap_006 = 12
    assert len(obtained[obtained["ID"] == "10-006"]) == expected_days_for_trap_006
    expected_last_day_trap_006 = "2025-01-12"
    assert expected_last_day_trap_006 in str(obtained[obtained["ID"] == "10-006"].Date.iloc[-1])
    expected_days_for_trap_007 = 14
    assert len(obtained[obtained["ID"] == "10-007"]) == expected_days_for_trap_007
    expected_days_for_trap_008 = 11
    assert len(obtained[obtained["ID"] == "10-008"]) == expected_days_for_trap_008
    expected_days_for_trap_009 = 4
    assert len(obtained[obtained["ID"] == "10-009"]) == expected_days_for_trap_009


def test_build_trap_daily_status_for_duplicated_positions():
    check_traps_log_with_duplicated_positions = pd.read_csv(
        "tests/data/check_traps_log_with_duplicated_position_id.csv"
    )
    obtained = build_trap_daily_status_for_duplicated_positions(
        check_traps_log_with_duplicated_positions, active_days
    )
    expected_days_for_trap_007 = 14
    assert len(obtained[obtained["ID"] == "10-007"]) == expected_days_for_trap_007
