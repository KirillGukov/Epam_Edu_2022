from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    num_sum_start = sum(nums[0:k])
    i = 0
    while k + i < len(nums):
        num_sum_end = sum(nums[(i+1):(k+i+1)])
        i += 1
        if num_sum_end >= num_sum_start:
            num_sum_start = num_sum_end
    nums_sum = num_sum_start
    return nums_sum
