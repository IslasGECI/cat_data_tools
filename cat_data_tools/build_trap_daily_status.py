import pandas as pd


def build_trap_daily_status(check_traps_log_df):
    check_traps_log_df["Date"] = pd.to_datetime(check_traps_log_df["Date"])
    df = check_traps_log_df[check_traps_log_df["Trap_status"] != "X"].copy()
    df_captures = check_traps_log_df[check_traps_log_df["Trap_status"] == "X"].copy()

    days_active = 7
    df["Date"] = df["Date"].apply(lambda x: pd.date_range(start=x, periods=days_active, freq="D"))
    df_exploded = df.explode("Date")
    df_exploded.drop_duplicates(subset=["ID", "Date"], keep="last", inplace=True)
    df_actives = df_exploded[df_exploded["Trap_status"] == "A"].copy()
    return pd.concat([df_actives, df_captures]).drop_duplicates(subset=["ID", "Date"], keep="last")
