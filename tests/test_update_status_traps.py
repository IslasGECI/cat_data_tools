from cat_data_tools.update_status_traps import _update_status_traps

import pandas as pd


def test_update_status_traps():
    traps_info_df = pd.DataFrame(
        {
            "Tipo": ["TC", "TC", "TC", "TL", "TC", "TC"],
            "ID": ["10-0008", "10-0006", "10-0006", "10-0006", "50-0006", "10-0006"],
            "Orden": [8, 8, 8, 8, 3, 8],
            "Fecha": [
                "2025-02-02",
                "2025-02-02",
                "2025-02-09",
                "2025-02-16",
                "2025-02-16",
                "2025-02-23",
            ],
        }
    )
    traps_info_df_cutted = traps_info_df.iloc[0:4]
    obtained = _update_status_traps(traps_info_df_cutted)
    expected_number_of_rows = 3
    assert (
        obtained.shape[0] == expected_number_of_rows
    ), f"Expected {expected_number_of_rows} rows, but got {obtained.shape[0]} rows"
    assert obtained.iloc[0]["Fecha"] == "2025-02-02"

    obtained = _update_status_traps(traps_info_df)
    expected_number_of_rows = 5
    assert (
        obtained.shape[0] == expected_number_of_rows
    ), f"Expected {expected_number_of_rows} rows, but got {obtained.shape[0]} rows"

    traps_info_df = pd.read_csv("tests/data/traps_info_for_tests.csv")
    obtained = _update_status_traps(traps_info_df)
    assert len(obtained) == 5
