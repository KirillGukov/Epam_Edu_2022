import pytest
from tasks.task_5 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([[1, 3, -1, -3, 5, 3, 6, 7], 3], 16),
        ([[7, 9, 4, -9, -3, 13, -4, 1], 4], 11)
    ]
)
def test_check_sum_of_four(value: list, expected_result: int):
    actual_result = find_maximal_subarray_sum(value[0], value[1])

    assert actual_result == expected_result
