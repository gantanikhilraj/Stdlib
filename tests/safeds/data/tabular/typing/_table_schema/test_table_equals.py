from safeds.data.tabular.containers import Table
from safeds.data.tabular.typing import FloatColumnType, IntColumnType, TableSchema
from tests.helpers import resolve_resource_path


def test_table_equals_valid() -> None:
    table = Table.from_json_file(resolve_resource_path("test_schema_table.json"))
    schema_expected = TableSchema(
        {
            "A": IntColumnType(),
            "B": IntColumnType(),
        }
    )

    assert table.schema == schema_expected


def test_table_equals_invalid() -> None:
    table = Table.from_json_file(resolve_resource_path("test_schema_table.json"))
    schema_not_expected = TableSchema(
        {
            "A": FloatColumnType(),
            "C": IntColumnType(),
        }
    )

    assert table.schema != schema_not_expected
