import pytest
from hw_1.tasks.task_3 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("file_name.txt", [1, 5]),
    ],
)
def test_find_maximum_and_minimum(value: str, expected_result: tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
