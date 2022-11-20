from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        line = fi.readline()
        max_num = int(line[0])
        min_num = int(line[0])
        f = line.strip().replace(', ', '')
        num = list(map(int, f))
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
            min_max: tuple[int, int] = (min_num, max_num)
            print(min_max)
            return min_max
