"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""

from typing import List, Tuple
from typing import Dict


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    list_nums: Dict[int, int] = {}
    for i in inp:
        if i not in list_nums:
            list_nums[i] = 1
        else:
            list_nums[i] += 1
    min_task_result = min(list_nums.items(), key=lambda item: item[1])
    max_task_result = max(list_nums.items(), key=lambda item: item[1])
    print(max_task_result[0], min_task_result[0])
    return max_task_result[0], min_task_result[0]
