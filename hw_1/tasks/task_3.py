from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        line = fi.readline()
        max_num = int(line[0])
        min_num = int(line[0])
        for i in fi:
            line_num = i.strip().split(",")
            num = list(map(int, line_num))
            for j in num:
                if max_num > j:
                    continue
                else:
                    max_num = j
            for s in num:
                if min_num < s:
                    continue
                else:
                    min_num = s
        min_max: Tuple[int, int] = (min_num, max_num)
        return min_max
