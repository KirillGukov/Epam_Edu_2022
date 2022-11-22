import pytest
from hw_1.tasks.task_5 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 16,),
        ([7, 5, 4, -9, -3, 13, -4, 1], 25,)
    ]
)
def test_check_sum_of_four(value: list, expected_result: int):
    actual_result = find_maximal_subarray_sum(value)

    assert actual_result == expected_result
