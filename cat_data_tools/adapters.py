import pandas as pd


class Adapter_for_dataframe:
    def __init__(self, path) -> None:
        self.path = path

    def get_dataframe(self):
        return pd.read_csv(self.path)
