def transform_effort_captures_to_dict(df, effort="esfuerzo", captures="capturas"):
    df_setup = setup_effort_captures_df_for_combination(df, effort, captures)
    effort_captures_dict = convert_dataframe_to_stan_dictonary(df_setup)
    return effort_captures_dict


def transform_effort_and_captures_from_cameras_and_traps_to_dict(df_traps, df_cameras):
    df_traps_to_combine = setup_effort_captures_df_for_combination(
        df_traps, "traps_effort", "captures"
    )
    df_cameras_to_combine = setup_effort_captures_df_for_combination(
        df_cameras, "cameras_effort", "detections"
    )

    combined = df_traps_to_combine.join(df_cameras_to_combine, how="inner")
    combined_dict = convert_dataframe_to_stan_dictonary(combined)
    return combined_dict


def convert_dataframe_to_stan_dictonary(df):
    df_dict = df.to_dict(orient="list")
    df_dict["T"] = len(df)
    return df_dict


def setup_effort_captures_df_for_combination(df, effort_name, captures_name):
    df_copy = df.copy()
    df_copy["Esfuerzo"] = df_copy.Esfuerzo.replace(0, 1)
    df_copy.set_index("Fecha", inplace=True)
    df_copy = df_copy[["Esfuerzo", "Capturas"]].rename(
        columns={"Esfuerzo": effort_name, "Capturas": captures_name}
    )
    return df_copy
