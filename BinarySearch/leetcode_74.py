"""
@Project ：LeetCode 
@File    ：leetcode_74.py
@Author  ：DZY
@Date    ：2025/4/15 13:00 
"""
import math
from typing import List

"""
74. 搜索二维矩阵
给你一个满足下述两条属性的 m x n 整数矩阵：
每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

示例 1：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

示例 2：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
"""


# 只用一次二分法
# 将矩阵每行拼接起来，但是实现上并不需要真正的拼接->用下标映射原矩阵的行号和列号
# 时间复杂度：O(log(mn))
def search_matrix(matrix: List[List[int]], target: int) -> bool:
    len_row = len(matrix)
    len_col = len(matrix[0])
    left, right = 0, len_row * len_col
    while left < right:
        mid = left + (right - left) // 2
        num = matrix[math.floor(mid / len_col)][mid % len_col]
        if num < target:
            left = mid + 1
        else:
            right = mid
    return True if left < len_row * len_col and matrix[math.floor(left / len_col)][left % len_col] == target else False

# todo
# 两次二分查找
# 对矩阵的第一列的元素二分查找，找到最后一个不大于目标值的元素，然后在该元素所在行中二分查找目标值是否存在。
# 时间复杂度：O(log(mn))


# 排除法
# 时间复杂度：O(m+n)
