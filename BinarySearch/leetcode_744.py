"""
@Project ：LeetCode 
@File    ：leetcode_744.py
@Author  ：DZY
@Date    ：2025/4/10 18:38 
"""

from typing import List

"""
744. 寻找比目标字母大的最小字母
给你一个字符数组 letters，该数组按非递减顺序排序，以及一个字符 target。letters 里至少有两个不同的字符。
返回 letters 中大于 target 的最小的字符。如果不存在这样的字符，则返回 letters 的第一个字符。

示例 1：
输入: letters = ["c", "f", "j"]，target = "a"
输出: "c"
解释：letters 中字典上比 'a' 大的最小字符是 'c'。

示例 2:
输入: letters = ["c","f","j"], target = "c"
输出: "f"
解释：letters 中字典顺序上大于 'c' 的最小字符是 'f'。

示例 3:
输入: letters = ["x","x","y","y"], target = "z"
输出: "x"
解释：letters 中没有一个字符在字典上大于 'z'，所以我们返回 letters[0]。
"""


def next_letter(letters: List[str], target: str) -> str:
    letters_length = len(letters)
    left, right = 0, letters_length
    while left < right:
        mid = left + (right - left) // 2
        letter = letters[mid]
        if letter <= target:
            left = mid + 1
        else:
            right = mid
    if left == letters_length:
        return letters[0]
    return letters[left]
