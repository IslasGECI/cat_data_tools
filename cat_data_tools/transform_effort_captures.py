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
    df_traps["Esfuerzo"] = df_traps.Esfuerzo.replace(0, 1)
    df_cameras["Esfuerzo"] = df_cameras.Esfuerzo.replace(0, 1)
    df_traps = df_traps[["Esfuerzo", "Capturas", "Fecha"]].rename(
        columns={"Esfuerzo": "traps_effort", "Capturas": "captures"}
    )
    df_cameras = df_cameras.rename(columns={"Esfuerzo": "cameras_effort", "Capturas": "detections"})
    df_traps.set_index("Fecha", inplace=True)
    df_cameras.set_index("Fecha", inplace=True)
    combined = df_traps.join(df_cameras, how="inner")
    combined_dict = combined.to_dict(orient="list")
    combined_dict["T"] = len(combined)
    return combined_dict
