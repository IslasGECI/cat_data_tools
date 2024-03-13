def join_trap_ids_and_daily_status(trap_daily_status, trap_ids):
    joined_dataframe = trap_daily_status.join(trap_ids.set_index("ID"), on="ID_de_trampa")
    return joined_dataframe
