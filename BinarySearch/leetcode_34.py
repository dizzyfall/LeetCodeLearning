"""
@Project ：LeetCode 
@File    ：leetcode_34.py
@Author  ：DZY
@Date    ：2025/4/10 20:59 
"""
from typing import List

"""
34. 在排序数组中查找元素的第一个和最后一个位置
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.get_first(nums, target)
        last = self.get_last(nums, target) - 1
        if first <= last and last < len(nums) and nums[first] == target and nums[last] == target:
            return [first, last]
        return [-1, -1]

    # 第一个大于等于target的下标
    def get_first(self, nums: List[int], target: int) -> int:
        length_nums = len(nums)
        left, right = 0, length_nums
        while left < right:
            mid = left + (right - left) // 2
            num = nums[mid]
            if num < target:
                left = mid + 1
            else:
                right = mid
        return left

    # 第一个大于target的下标
    def get_last(self, nums: List[int], target: int) -> int:
        length_nums = len(nums)
        left, right = 0, length_nums
        while left < right:
            mid = left + (right - left) // 2
            num = nums[mid]
            if num <= target:
                left = mid + 1
            else:
                right = mid
        return left
