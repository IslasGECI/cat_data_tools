def calculate_effort_and_captures(data):
    data_copy = data.copy()
    data_copy["Zone"] = data_copy["ID"].str.split("-").str[0]
    summary = data_copy.groupby(["Date", "Zone"]).agg(Effort=("ID", "size")).reset_index()
    return summary
