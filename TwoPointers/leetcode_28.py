"""
@Project ：LeetCode 
@File    ：leetcode_28.py
@Author  ：DZY
@Date    ：2025/6/10 10:23 
"""

"""
28. 找出字符串中第一个匹配项的下标
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。

示例 1：
输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。

示例 2：
输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。

提示：
1 <= haystack.length, needle.length <= 104
haystack 和 needle 仅由小写英文字符组成
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        for i in range(h_len - n_len + 1):
            h_p, n_p = i, 0
            while n_p < n_len and haystack[h_p] == needle[n_p]:
                h_p += 1
                n_p += 1
            if n_p == n_len:
                return i
        return -1


s = Solution()
haystack = "leetcode"
needle = "leeto"
s.strStr(haystack, needle)

# KMP算法
