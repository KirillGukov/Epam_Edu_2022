from hw_3.tasks.task_2 import decorator_calculate
from time import time


def test_decorator():
    first = time()
    decorator_calculate(500)
    actual_result = time() - first
    assert actual_result < 60
