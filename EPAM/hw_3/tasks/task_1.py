"""In previous homework task 4, you wrote a cache function that remembers other function output value. Modify it to be
a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass

Would give out cached value up to times number only. Example:
@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

f()
? 1
'1'
f()      #will remember previous value
'1'
f()      #but use it up to two times only
'1'
f()
? 2
'2'
"""


from collections.abc import Callable


def cache(times=None) -> Callable:
    def decorator_funct(func):
        dict_func = {}
        if times:
            func_num = times

        def second_funct(*args, **kwargs):
            if (tuple(args), tuple(kwargs.items())) in dict_func:
                nonlocal func_num
                if func_num > 1:
                    func_num -= 1
                    return dict_func[(tuple(args), tuple(kwargs.items()))]
                else:
                    return dict_func.pop(tuple(args), tuple(kwargs.items()))
            else:
                dict_func[tuple(args), tuple(kwargs.items())] = func(*args, **kwargs)
                return dict_func[tuple(args), tuple(kwargs.items())]
        return func_num
    return decorator_funct
