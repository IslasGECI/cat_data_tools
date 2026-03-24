def get_status_change(daily_status_df):
    daily_status_df_copy = daily_status_df.copy().dropna(subset="Trap_status")
    df = daily_status_df_copy.sort_values(by=["ID", "Date"])
    is_status_changed = df["Trap_status"] != df.groupby("ID")["Trap_status"].shift()
    is_trapper_changed = df["Trapper"] != df.groupby("ID")["Trapper"].shift()
    is_type_changed = df["Type"] != df.groupby("ID")["Type"].shift()
    filtered_df = df.loc[is_status_changed | is_trapper_changed | is_type_changed]
    return filtered_df.reset_index(drop=True)


def add_next_status_column(daily_status_df):
    sorted_daily = daily_status_df.sort_values(["ID", "Type", "Trapper", "Date"])
    sorted_daily["next_status"] = sorted_daily.groupby(["ID", "Type", "Trapper"])[
        "Trap_status"
    ].shift(-1)
    return sorted_daily
