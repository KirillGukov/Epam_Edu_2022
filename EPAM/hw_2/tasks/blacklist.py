import string


def custom_range(iterable, *args, step=1) -> list:
    """
    :param iterable: must be some iterable obj
    :param args: items from iterable
    :return: list[start : end : step] from iterable
    """
    try:
        iter(iterable)
    except TypeError:
        print("first arg must be iterable")
    if len(args) == 1:
        end = args[0]
        start = iterable[0]
    if len(args) == 2:
        start, end = args
    if len(args) == 3:
        start, end, step = args

        result_list = [i for i in iterable[iterable.index(start): iterable.index(end): step]]
        return result_list


custom_range(string.ascii_lowercase, "g")
