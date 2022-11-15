from time import sleep
from hw_2.tasks.task_4 import cache


def value(*args):
    sleep(0.5)
    return sum(args)


def summ_try(a, b):
    sleep(0.5)
    return a + b


def test_value_try():
    value1 = 1
    value2 = 2
    cache_func = cache(value)
    actual_result1 = cache_func(value1, value2)
    actual_result2 = cache_func(value1, value2)

    assert actual_result1 is actual_result2


def test_summ_try():
    cache_func = cache(value)
    actual_result = cache_func()

    assert actual_result is actual_result
