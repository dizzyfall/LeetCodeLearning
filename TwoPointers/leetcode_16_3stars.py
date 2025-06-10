"""
@Project ：LeetCode 
@File    ：leetcode_16_3stars.py
@Author  ：DZY
@Date    ：2025/5/14 12:37 
"""

from typing import List

"""
16. 最接近的三数之和
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
返回这三个数的和。
假定每组输入只存在恰好一个解。

示例 1：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。

示例 2：
输入：nums = [0,0,0], target = 1
输出：0
解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。

提示：
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""


# 双指针
def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    # 初始化必须很大，不能是target，因为：
    # 第一：三个数加起来不一定就等于target，可能给定的数组三个数无论怎么加都不等于target，只能接近target，而这时ans是不会更新的，永远都是target，最后的答案就是错的
    # 第二：最接近是绝对值，可以从target的左边或者右边接近
    ans = 10 ** 7
    for i in range(n):
        left, right = i + 1, n - 1
        while left < right:
            cur = nums[i] + nums[left] + nums[right]
            if abs(cur - target) < abs(ans - target):
                ans = cur
            if cur == target:
                return cur
            elif cur < target:
                left += 1
            else:
                right -= 1
    return ans
