"""
@Project ：LeetCode 
@File    ：leetcode_11_5stars.py
@Author  ：DZY
@Date    ：2025/5/12 13:41 
"""
from typing import List

"""
11. 盛最多水的容器
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。

示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2：
输入：height = [1,1]
输出：1

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

# 双指针
"""
思路：
这道题和接雨水（leetcode_42)比较像
水的面积由两端更短的木板和两端木板长度共同决定，利用双指针，两个指针分别指向两端，在移动指针时，必须固定其中一个指针，移动另一个指针，不能同时移动，因为不知道什么条件可以同时移动指针
那什么时候移动左指针，什么时候移动右指针呢？
直觉是每次应该移动木板长度比较小的指针，因为水面积是（更短的木板*两个木板之间长度），如果移动长的木板，水面积的两个木板长度减小，更短木板不变，总的水面积必定减小，但是我们要找最大水面积，因此一定是移动更短的木板
"""


def maxArea(self, height: List[int]) -> int:
    left, right = 0, len(height) - 1
    ans = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        ans = max(ans, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return ans
