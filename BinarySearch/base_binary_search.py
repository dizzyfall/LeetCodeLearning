"""
@Project ：LeetCode
@File    ：base_binary_search.py
@Author  ：DZY
@Date    ：2025/4/10 14:56
"""
from typing import List

"""
704. 二分查找
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1

示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
"""


# 第一种基础的写法
def base_search_one(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        num = nums[mid]
        if num == target:
            return mid
        elif target < num:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# 第二种基础的写法
def base_search_two(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        num = nums[mid]
        if target == num:
            return mid
        elif target < num:
            right = mid
        else:
            left = mid + 1
    return -1
