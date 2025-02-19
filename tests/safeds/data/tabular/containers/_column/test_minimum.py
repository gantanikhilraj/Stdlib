import pandas as pd
import pytest
from safeds.data.tabular.containers import Table
from safeds.exceptions import NonNumericColumnError


def test_minimum_invalid() -> None:
    with pytest.raises(NonNumericColumnError):
        table = Table(pd.DataFrame(data={"col1": ["col1_1", 2]}))
        column = table.get_column("col1")
        column.minimum()


def test_minimum_valid() -> None:
    table = Table(pd.DataFrame(data={"col1": [1, 2, 3, 4]}))
    column = table.get_column("col1")
    assert column.minimum() == 1
