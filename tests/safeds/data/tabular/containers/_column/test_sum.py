import pandas as pd
import pytest
from safeds.data.tabular.containers import Column
from safeds.exceptions import NonNumericColumnError


def test_sum_valid() -> None:
    c1 = Column(pd.Series([1, 2]), "test")
    assert c1.sum() == 3


def test_sum_invalid() -> None:
    c1 = Column(pd.Series([1, "a"]), "test")
    with pytest.raises(NonNumericColumnError):
        c1.sum()
