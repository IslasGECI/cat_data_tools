def select_captures_from_daily_status(daily_status):
    return daily_status[daily_status["Estado_trampa"] == "X"]
