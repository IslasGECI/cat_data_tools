from cat_data_tools.transform_effort_captures import transform_effort_captures_to_dict
import pandas as pd


def test_transform_effort_captures_to_dict():
    obtained = transform_effort_captures_to_json(df)
    expected_keys = ["T", "esfuerzo", "capturas"]
    assert list(obtained.keys()) == expected_keys
