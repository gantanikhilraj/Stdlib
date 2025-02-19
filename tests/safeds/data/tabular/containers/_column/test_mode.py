import pandas as pd
from safeds.data.tabular.containers import Table


def test_mode_valid() -> None:
    table = Table(pd.DataFrame(data={"col1": [1, 2, 3, 4, 3]}))
    column = table.get_column("col1")
    assert column.mode() == [3]


def test_mode_valid_str() -> None:
    table = Table(pd.DataFrame(data={"col1": ["1", "2", "3", "4", "3"]}))
    column = table.get_column("col1")
    assert column.mode() == ["3"]


def test_mode_valid_list() -> None:
    table = Table(pd.DataFrame(data={"col1": ["1", "4", "3", "4", "3"]}))
    column = table.get_column("col1")
    assert column.mode() == ["3", "4"]
