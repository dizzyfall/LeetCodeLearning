"""
@Project ：LeetCode 
@File    ：leetcode_69.py
@Author  ：DZY
@Date    ：2025/4/15 15:42 
"""
"""
69. x 的平方根 
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
由于返回类型是整数，结果只保留整数部分 ，小数部分将被舍去 。
注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

示例 1：
输入：x = 4
输出：2

示例 2：
输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。

0 <= x <= 231 - 1
"""


def get_sqrt(x: int) -> int:
    left, right = 0, x + 1
    while left < right:
        mid = left + (right - left) // 2
        target = mid * mid
        if x >= target:
            left = mid + 1
        else:
            right = mid
    return left - 1
