from safeds.data.tabular.containers import Row
from safeds.data.tabular.typing import IntColumnType, StringColumnType, TableSchema


def test_count() -> None:
    row = Row(
        [0, "1"],
        TableSchema(
            {"testColumn1": IntColumnType(), "testColumn2": StringColumnType()}
        ),
    )
    assert len(row) == 2
