import pandas as pd


def build_trap_daily_status(check_traps_log_df):
    df = check_traps_log_df.copy()
    df["Date"] = pd.to_datetime(df["Date"])

    df_activos = df[df["Trap_status"] == "A"]
    days_active = 7
    df_activos["Date"] = df_activos["Date"].apply(
        lambda x: pd.date_range(start=x, periods=days_active, freq="D")
    )
    return df_activos.explode("Date").drop_duplicates(subset=["ID", "Date"])
