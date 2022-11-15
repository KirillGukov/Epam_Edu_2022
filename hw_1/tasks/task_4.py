from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    tup_count = 0
    for i in range(len(a)):
        if a[i] + b[i] + c[i] + d[i] == 0:
            tup_count += 1
    return tup_count
