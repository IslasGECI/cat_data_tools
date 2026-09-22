def transform_effort_captures_to_dict(df, effort="esfuerzo", captures="capturas"):
    df["Esfuerzo"] = df.Esfuerzo.replace(0, 1)
    effort_captures_dict = (
        df[["Esfuerzo", "Capturas"]]
        .rename(columns={"Esfuerzo": effort, "Capturas": captures})
        .to_dict(orient="list")
    )
    effort_captures_dict["T"] = len(df)
    return effort_captures_dict


def transform_effort_and_captures_from_cameras_and_traps_to_dict(df_traps, df_cameras):
    traps_dict = transform_effort_captures_to_dict(
        df_traps, effort="traps_effort", captures="captures"
    )
    cameras_dict = transform_effort_captures_to_dict(
        df_cameras, effort="cameras_effort", captures="detections"
    )
    traps_dict.update(cameras_dict)
    return traps_dict
