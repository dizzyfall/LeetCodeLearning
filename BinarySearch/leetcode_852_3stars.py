"""
@Project ：LeetCode 
@File    ：leetcode_852_3stars.py
@Author  ：DZY
@Date    ：2025/4/17 11:38 
"""
from typing import List

"""
852. 山脉数组的峰顶索引
给定一个长度为 n 的整数 山脉 数组 arr ，其中的值递增到一个 峰值元素 然后递减。
返回峰值元素的下标。
你必须设计并实现时间复杂度为 O(log(n)) 的解决方案。

示例 1：
输入：arr = [0,1,0]
输出：1

示例 2：
输入：arr = [0,2,1,0]
输出：1

示例 3：
输入：arr = [0,10,5,2]
输出：1
 
3 <= arr.length <= 105
0 <= arr[i] <= 106
题目数据 保证 arr 是一个山脉数组
"""


def peak_index_in_mountain_array(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


print(peak_index_in_mountain_array([0, 3, 5, 12, 2]))
