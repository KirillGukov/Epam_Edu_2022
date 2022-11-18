import pytest
from hw_1.tasks.task_2 import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([0, 1, 1, 2, 3, 5, 8, 13], True),
        ([19, 27, 132, 84, 3], False),
        ([13, 21, 34, 55, 89], True),
        ([0, 0], False),
    ],
)
def test_check_fibonacci(value: [int], expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
