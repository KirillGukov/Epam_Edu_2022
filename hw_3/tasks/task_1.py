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


def decorator_funct(func):
    def wrapper():
        func()
    return wrapper


@decorator_funct
def cache(function: Callable, dct={}):


    def second_funct(*args, **kwargs):
        if function in dct:
            return dct[function]
        else:
            dct[function] = function()
            return dct[function]
    return second_funct
