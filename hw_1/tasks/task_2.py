from collections.abc import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    s = False
    if len(data) > 2:
        for i in range(2, len(data)):
            if data[i] == data[i - 1] + data[i - 2]:
                s = True
            else:
                break

    if s:
        return True
    else:
        return False
