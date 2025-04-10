"""
@Project ：LeetCode 
@File    ：leetcode_1351.py
@Author  ：DZY
@Date    ：2025/4/10 18:58 
"""
from typing import List

"""
1351. 统计有序矩阵中的负数
给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非严格递减顺序排列。 请你统计并返回 grid 中 负数 的数目。

示例 1：
输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
输出：8
解释：矩阵中共有 8 个负数。

示例 2：
输入：grid = [[3,2],[1,0]]
输出：0
"""


def count_negatives(grid: List[List[int]]) -> int:
    count = 0
    for row in grid:
        length_row = len(row)
        left, right = 0, length_row
        while left < right:
            mid = left + (right - left) // 2
            num = row[mid]
            if num >= 0:
                left = mid + 1
            else:
                right = mid
        count_row = length_row - (left + 1) + 1
        count += count_row
    return count

# todo 分治算法
# todo 时间复杂度为O(m+n)的算法
