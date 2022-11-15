import pytest
from hw_2.tasks.task_2 import major_and_minor_elem


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
        ([3, 2, 3], (3, 2)),
        ([6, 5, 8, 4, 9, 0, 1, 7, 2, 0], (0, 6)),
    ],
)
def test_major_and_minor_elem(value: list, expected_result: tuple):
    actual_result = major_and_minor_elem(value)

    assert actual_result == expected_result
