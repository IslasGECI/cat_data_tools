def update_status_traps(traps_info_df):
    return traps_info_df.drop_duplicates(subset=["Tipo", "ID", "Orden"], keep="first").reset_index(
        drop=True
    )
