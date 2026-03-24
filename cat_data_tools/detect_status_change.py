def get_status_change(daily_status_df):
    daily_status_df_copy = daily_status_df.copy().dropna(subset="Trap_status")
    df = daily_status_df_copy.sort_values(by=["ID", "Date"])
    is_status_changed = df["Trap_status"] != df.groupby("ID")["Trap_status"].shift()
    is_trapper_changed = df["Trapper"] != df.groupby("ID")["Trapper"].shift()
    is_type_changed = df["Type"] != df.groupby("ID")["Type"].shift()
    filtered_df = df.loc[is_status_changed | is_trapper_changed | is_type_changed]
    return filtered_df.reset_index(drop=True)


def compute_trap_check_log(daily_status_df):
    daily_status_with_next_status = add_next_status_column(daily_status_df)
    check_log = subsitute_check_traps_status(daily_status_with_next_status)
    columns_list = [
        "Date",
        "Type",
        "ID",
        "Trapper",
        "Trap_status",
        "Bait",
        "Nombre_del_responsable",
    ]
    return check_log[columns_list]


def add_next_status_column(daily_status_df):
    sorted_daily = daily_status_df.sort_values(["ID", "Type", "Trapper", "Date"])
    sorted_daily["next_status"] = sorted_daily.groupby(["ID", "Type", "Trapper"])[
        "Trap_status"
    ].shift(-1)
    is_capture = sorted_daily["Trap_status"] == "RX"
    sorted_daily.loc[is_capture, "next_status"] = "X"
    return sorted_daily


def subsitute_check_traps_status(df):
    checked_traps = df[df.Trap_status.str.startswith("R")]
    checked_traps.Trap_status = checked_traps.next_status
    return checked_traps
