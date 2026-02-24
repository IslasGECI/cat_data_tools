def transform_effort_captures_to_dict(df):
    df["Esfuerzo"] = df.Esfuerzo.replace(0, 1)
    effort_captures_dict = (
        df[["Esfuerzo", "Capturas"]]
        .rename(columns={"Esfuerzo": "esfuerzo", "Capturas": "capturas"})
        .to_dict(orient="list")
    )
    effort_captures_dict["T"] = len(df)
    return effort_captures_dict
