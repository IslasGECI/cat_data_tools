def calculate_effort_and_captures(data):
    data_copy = data.copy()
    data_copy["is_capture"] = data_copy["Trap_status"] == "X"
    data_copy["Zone"] = data_copy["ID"].str.split("-").str[0]
    summary = (
        data_copy.groupby(["Date", "Zone"])
        .agg(Effort=("ID", "size"), Captures=("is_capture", "sum"))
        .reset_index()
    )

    return summary
