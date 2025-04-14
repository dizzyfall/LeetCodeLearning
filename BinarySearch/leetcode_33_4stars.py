"""
@Project ：LeetCode 
@File    ：leetcode_33_4stars.py
@Author  ：DZY
@Date    ：2025/4/14 16:00 
"""
from typing import List

"""
33. 搜索旋转排序数组
整数数组 nums 按升序排列，数组中的值互不相同。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了旋转，
使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你旋转后的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：
输入：nums = [1], target = 0
输出：-1
"""


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        num = nums[mid]
        if num == target:
            return mid
        # 范围分为[left,mid],[mid+1,right]
        # 用nums[0]<=num条件来判断[left,mid]是否为有序数组，是，则有序，反之，无无序
        # 会不会出现一种情况：即使nums[0]<=num，但数组可能是无序的，比如[2,6,3,4]，但是想了想这个数组的构建不符合题意（按题目的意思是构建不出来这种数组的）
        if nums[0] <= num:
            if nums[0] <= target < num:
                right = mid
            else:
                left = mid + 1
        else:
            if num < target <= nums[len(nums) - 1]:
                left = mid + 1
            else:
                right = mid
    return -1
