from cat_data_tools.transform_effort_captures import (
    transform_effort_captures_to_dict,
    transform_effort_and_captures_from_cameras_and_traps_to_dict,
)
import pandas as pd

df_traps = pd.read_csv("tests/data/esfuerzo_capturas_mensuales_gatos_socorro_3_years.csv")
df_cameras = pd.read_csv("tests/data/monthly_cameras_effort_and_captures.csv")


def test_transform_effort_captures_to_dict():
    obtained = transform_effort_captures_to_dict(df_traps)
    expected_keys = ["T", "esfuerzo", "capturas"]
    assert set(obtained.keys()) == set(expected_keys)
    are_effort_zero = 0 in obtained["esfuerzo"]
    assert not are_effort_zero, "There should be no zero values in the effort list"


def test_transform_effort_and_captures_from_cameras_and_traps_to_dict():
    obtained = transform_effort_and_captures_from_cameras_and_traps_to_dict(df_traps, df_cameras)
