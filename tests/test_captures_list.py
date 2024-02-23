from cat_data_tools import join_trap_info_with_captures, select_captures_from_daily_status
import pandas as pd


def test_select_captures_from_daily_status():
    daily_status = pd.read_csv("tests/data/trap_daily_status.csv")
    obtained = select_captures_from_daily_status(daily_status)
    expected_captures = 2
    assert len(obtained) == expected_captures


def tests_join_trap_info_with_captures():
    traps_info = pd.DataFrame(
        {
            "ID_de_trampa": ["TC-01-2156-MV", "TC-02-2156-MO", "TC-01-2157-NR"],
            "latitude": [19, 20, 21],
            "longitude": [-118, -120, -121],
        }
    )

    obtained = join_trap_info_with_captures(captures, traps_info)
    expected_len = 3
    assert len(obtained) == expected_len


captures = pd.DataFrame(
    {
        "ID_de_trampa": ["TC-01-2156-MV", "TC-02-2156-MO", "TC-01-2156-MV"],
        "Estado_trampa": ["X", "X", "X"],
        "Fecha": ["10/Sep/2023", "10/Sep/2023", "19/Sep/2023"],
    }
)
