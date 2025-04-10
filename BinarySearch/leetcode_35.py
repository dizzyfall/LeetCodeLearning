"""
@Project ：LeetCode 
@File    ：leetcode_35.py
@Author  ：DZY
@Date    ：2025/4/10 17:02 
"""
from typing import List

"""
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法

示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2

示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1

示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4
"""


def search_insert_one(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        num = nums[mid]
        if target > num:
            left = mid + 1
        else:
            right = mid
    return left


def search_insert_two(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        num = nums[mid]
        if target > num:
            left = mid + 1
        else:
            right = mid - 1
    return left
