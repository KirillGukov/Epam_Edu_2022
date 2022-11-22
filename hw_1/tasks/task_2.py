from collections.abc import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return False
    else:
        for i in range(2, len(data)):
            if data[i] != data[i - 1] + data[i - 2] or data[i] <= data[i - 2]:
                return False
            else:
                return True
