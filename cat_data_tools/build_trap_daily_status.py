import pandas as pd


def build_trap_daily_status(check_traps_log_df, days_active):
    socorro_unique_trap_identificators = ["ID", "Date", "Type"]

    check_traps_log_df["Date"] = pd.to_datetime(check_traps_log_df["Date"])
    df = check_traps_log_df[check_traps_log_df["Trap_status"] != "X"].copy()
    df_captures = check_traps_log_df[check_traps_log_df["Trap_status"] == "X"].copy()

    df["Date"] = df["Date"].apply(lambda x: pd.date_range(start=x, periods=days_active, freq="D"))
    df_exploded = df.explode("Date")

    df_exploded.drop_duplicates(
        subset=socorro_unique_trap_identificators, keep="last", inplace=True
    )
    df_actives = df_exploded[df_exploded["Trap_status"] == "A"].copy()
    concatenated_catpures = pd.concat([df_actives, df_captures]).drop_duplicates(
        subset=socorro_unique_trap_identificators, keep="last"
    )
    return concatenated_catpures.sort_values(by=["ID", "Date"]).reset_index(drop=True)


def build_trap_daily_status_for_duplicated_positions(check_traps_log_df, days_active):
    guadalupe_unique_trap_indentificators = ["ID", "Date", "Type", "Trapper"]

    check_traps_log_df["Date"] = pd.to_datetime(check_traps_log_df["Date"])
    df = check_traps_log_df[check_traps_log_df["Trap_status"] != "X"].copy()
    df_captures = check_traps_log_df[check_traps_log_df["Trap_status"] == "X"].copy()

    df["Date"] = df["Date"].apply(lambda x: pd.date_range(start=x, periods=days_active, freq="D"))
    df_exploded = df.explode("Date")

    df_exploded.drop_duplicates(
        subset=guadalupe_unique_trap_indentificators, keep="last", inplace=True
    )
    df_actives = df_exploded[df_exploded["Trap_status"] == "A"].copy()
    concatenated_catpures = pd.concat([df_actives, df_captures]).drop_duplicates(
        subset=guadalupe_unique_trap_indentificators, keep="last"
    )
    return concatenated_catpures.sort_values(by=["ID", "Date"]).reset_index(drop=True)
