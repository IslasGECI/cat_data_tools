import pandas as pd


def build_trap_daily_status(check_traps_log_df):
    df = check_traps_log_df.copy()
    df["Date"] = pd.to_datetime(df["Date"])

    days_active = 7
    df["Date"] = df["Date"].apply(lambda x: pd.date_range(start=x, periods=days_active, freq="D"))
    df_exploded = df.explode("Date")
    df_exploded.drop_duplicates(subset=["ID", "Date"], keep="last", inplace=True)
    return df_exploded[df_exploded["Trap_status"] == "A"].copy()
