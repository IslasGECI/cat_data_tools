from cat_data_tools.transform_effort_captures import transform_effort_captures_to_dict
import pandas as pd


def test_transform_effort_captures_to_dict():
    df = pd.read_csv("tests/data/esfuerzo_capturas_mensuales_gatos_socorro_3_years.csv")
    obtained = transform_effort_captures_to_dict(df)
    expected_keys = ["T", "esfuerzo", "capturas"]
    assert set(obtained.keys()) == set(expected_keys)
