"""
@Project ：LeetCode 
@File    ：leetcode_300_5stars.py
@Author  ：DZY
@Date    ：2025/4/23 15:24 
"""
from typing import List

"""
300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1
 

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
"""


# 动态规划
# dp[i]表示的是以第i个元素结尾的子序列最大长度
# 时间复杂度O(n^2)
# 空间复杂度O(n)
def length_longest_increasing_subsequence(nums: List[int]) -> int:
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# 动态规划+二分法（方法一的优化）
# 时间复杂度O(nlogn)
# 空间复杂度O(n)
