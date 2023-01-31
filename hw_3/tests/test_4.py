from hw_3.tasks.task_4 import is_armstrong
import pytest


@pytest.mark.parametrize(["number", "expected_result"], [(153, True), (12, False), (10, False), (9, True)],)
def test_is_armstrong(number: int, expected_result: bool):
    assert is_armstrong(153) == True
    assert is_armstrong(12) == False
    assert is_armstrong(10) == False
    assert is_armstrong(9) == True
