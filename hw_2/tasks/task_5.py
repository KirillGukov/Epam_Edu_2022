"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""


def custom_range(iterable, *args, **kwargs):
    if len(args) == 1:
        first = iterable[0]
        last = args[0]
        result_one = [i for i in iterable[iterable.index(first): iterable.index(last)]]
        return result_one
    if len(args) == 2:
        first, last = args
        result_two = [i for i in iterable[iterable.index(first): iterable.index(last)]]
        return result_two
    if len(args) == 3:
        first, last, step = args
        resul_three = [i for i in iterable[iterable.index(first): iterable.index(last): step]]
        return resul_three
