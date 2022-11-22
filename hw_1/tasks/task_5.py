from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    s = 0
    for _ in nums:
        while s < k:
            a = max(nums)
            max_sum += a
            nums.remove(a)
            s += 1
    print(max_sum)
