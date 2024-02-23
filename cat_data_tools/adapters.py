import pandas as pd


def Adapter_for_path_to_dataframe(path):
    return Adapter_from_csv_path(path)


class Adapter_from_csv_path:
    def __init__(self, path) -> None:
        self.path = path

    def get_dataframe(self):
        return "from_csv"


class Adapatador_from_empty_path:
    def __init__(self):
        self.get_list_traps = None
        self.lista_trampas = self.get_list_traps

    def get_dataframe(self):
        return self.lista_trampas
