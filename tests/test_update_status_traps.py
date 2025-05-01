from cat_data_tools.update_status_traps import update_status_traps

import pandas as pd


def test_update_status_traps():
    traps_info_df = pd.DataFrame(
        {
            "Tipo": ["TC", "TC", "TC", "TL", "TC"],
            "ID": ["10-0008", "10-0006", "10-0006", "10-0006", "10-0006"],
            "Orden": [8, 8, 8, 8, 8],
            "Fecha": ["2025-02-02", "2025-02-02", "2025-02-09", "2025-02-16", "2025-02-23"],
        }
    )
    traps_info_df_cutted = traps_info_df.iloc[0:4]
    print(traps_info_df_cutted)
    obtained = update_status_traps(traps_info_df_cutted)
    expected_number_of_rows = 3
    assert (
        obtained.shape[0] == expected_number_of_rows
    ), f"Expected {expected_number_of_rows} rows, but got {obtained.shape[0]} rows"
