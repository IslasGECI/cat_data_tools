import pandas as pd


def build_trap_daily_status(check_traps_log_df, days_active):
    socorro_unique_trap_identificators = ["ID", "Date", "Type"]
    concatenated_captures_sorted = fill_trap_daily_status(
        check_traps_log_df, days_active, socorro_unique_trap_identificators
    )
    return concatenated_captures_sorted


def build_trap_daily_status_for_duplicated_positions(check_traps_log_df, days_active):
    guadalupe_unique_trap_indentificators = ["ID", "Date", "Type", "Trapper"]
    concatenated_captures_sorted = fill_trap_daily_status(
        check_traps_log_df, days_active, guadalupe_unique_trap_indentificators
    )
    return concatenated_captures_sorted


def fill_trap_daily_status(check_traps_log_df, days_active, unique_trap_identificators):
    df_actives = activate_traps_for_n_days(
        check_traps_log_df, days_active, unique_trap_identificators
    )
    df_captures = check_traps_log_df[check_traps_log_df["Trap_status"] == "X"].copy()
    concatenated_captures_sorted = concatenate_captures_and_actives(
        df_captures, df_actives, unique_trap_identificators
    )
    return concatenated_captures_sorted


def activate_traps_for_n_days(check_traps_log_df, days_active, unique_trap_identificators):
    check_traps_log_df["Date"] = pd.to_datetime(check_traps_log_df["Date"])
    df = check_traps_log_df[check_traps_log_df["Trap_status"] != "X"].copy()

    df["Date"] = df["Date"].apply(lambda x: pd.date_range(start=x, periods=days_active, freq="D"))
    df_exploded = df.explode("Date")

    df_exploded.drop_duplicates(subset=unique_trap_identificators, keep="last", inplace=True)
    df_actives = df_exploded[df_exploded["Trap_status"] == "A"].copy()
    return df_actives


def concatenate_captures_and_actives(df_captures, active_traps_df, unique_trap_identificators):
    concatenated_catpures = pd.concat([active_traps_df, df_captures]).drop_duplicates(
        subset=unique_trap_identificators, keep="last"
    )
    concatenated_captures_sorted = concatenated_catpures.sort_values(by=["ID", "Date"]).reset_index(
        drop=True
    )
    return concatenated_captures_sorted
