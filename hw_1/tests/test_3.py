import pytest
import os
from tasks.task_3 import find_maximum_and_minimum
path = os.path.dirname(os.path.abspath(__file__)) + "/file_name.txt"


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (path, (1, 6)),
    ],
)
def test_find_maximum_and_minimum(value: str, expected_result: tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
