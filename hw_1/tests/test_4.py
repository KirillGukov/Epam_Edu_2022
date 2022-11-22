import pytest
from hw_1.tasks.task_4 import check_sum_of_four


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (
            [
                [0, 1, 1, 2],
                [4, 5, 6, 7],
                [-2, 7, -8, 13],
                [-2, 9, 1, -6]
            ],
            2,
        ),
        (
            [
                [-3, 7, 4],
                [-2, 5, 1],
                [11, 6, 3],
                [9, -18, -5]
            ],
            2,
        )
    ]
)
def test_check_sum_of_four(value: list, expected_result: int):
    actual_result = check_sum_of_four(value)

    assert actual_result == expected_result
