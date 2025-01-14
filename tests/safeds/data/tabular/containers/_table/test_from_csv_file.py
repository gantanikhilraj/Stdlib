import pytest
from safeds.data.tabular.containers import Table
from tests.helpers import resolve_resource_path


def test_from_csv_file_valid() -> None:
    table = Table.from_csv_file(resolve_resource_path("test_table_from_csv_file.csv"))
    assert table.get_column("A").get_value(0) == 1 and table.get_column("B").get_value(0) == 2


def test_from_csv_file_invalid() -> None:
    with pytest.raises(FileNotFoundError):
        Table.from_csv_file(resolve_resource_path("test_table_from_csv_file_invalid.csv"))
