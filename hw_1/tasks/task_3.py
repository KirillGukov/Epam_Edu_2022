from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        line = fi.readline()

        f = line.strip().split(",")
        num = list(map(int, f))
        max_num = num[0]
        min_num = num[0]
        for i in num:
            if max_num > int(i):
                continue
            else:
                max_num = i
        for j in num:
            if min_num < int(j):
                continue
            else:
                min_num = j
        res_nums = (min_num, max_num)
        return res_nums
