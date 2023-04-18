from hw_3.tasks.task_1 import cache


@cache(times=2)
def f():
    return input('? ')


def test_decor_func():
    actual_result_1 = cache('? ')
    actual_result_2 = cache('? ')

    assert actual_result_1 is actual_result_2
