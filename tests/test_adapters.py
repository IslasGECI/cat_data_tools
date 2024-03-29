from cat_data_tools import Adapter_for_path_to_dataframe
import pandas as pd


def test_adapter_path_to_dataframe():
    path = "tests/data/trap_daily_status.csv"
    adapter = Adapter_for_path_to_dataframe(path)
    obtained = adapter.get_dataframe()
    assert isinstance(obtained, pd.DataFrame)

    path = ""
    adapter = Adapter_for_path_to_dataframe(path)
    obtained = adapter.get_dataframe()
    assert isinstance(obtained, pd.DataFrame)
