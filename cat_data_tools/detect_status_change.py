def get_status_change(daily_status_df):
    df = daily_status_df.sort_values(by=["ID", "Date"])
    is_status_changed = df["Trap_status"] != df["Trap_status"].shift()
    filtered_df = df.loc[is_status_changed]
    return filtered_df.reset_index(drop=True)
