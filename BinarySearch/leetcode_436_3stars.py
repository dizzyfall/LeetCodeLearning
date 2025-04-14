"""
@Project ：LeetCode 
@File    ：leetcode_436_3stars.py
@Author  ：DZY
@Date    ：2025/4/11 14:56 
"""
from typing import List

"""
436. 寻找右区间
给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。
区间 i 的 右侧区间 是满足 startj >= endi，且 startj 最小 的区间 j。注意 i 可能等于 j 。
返回一个由每个区间 i 对应的 右侧区间 下标组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 -1 。

示例 1：
输入：intervals = [[1,2]]
输出：[-1]
解释：集合中只有一个区间，所以输出-1。

示例 2：
输入：intervals = [[3,4],[2,3],[1,2]]
输出：[-1,0,1]
解释：对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点。

示例 3：
输入：intervals = [[1,4],[2,3],[3,4]]
输出：[-1,2,-1]
解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间 [3,4] 有最小的“右”起点。
"""


# 给定的数据种每个区间开头所组成的列表可以是升序的也可以是降序的，需要统一变为升序（好做）
# 例如示例二是[3,2,1]，而示例三是[1,2,3]

def find_right_interval(intervals: List[List[int]]) -> List[int]:
    first_intervals = []
    res = []
    for index, interval in enumerate(intervals):
        first_intervals.append([index, interval[0]])

    sorted_first_intervals = sorted(first_intervals, key=lambda x: x[1])

    for interval in intervals:
        length_first_intervals = len(sorted_first_intervals)
        left, right = 0, length_first_intervals
        target = interval[1]
        while left < right:
            mid = left + (right - left) // 2
            num = sorted_first_intervals[mid][1]
            if num < target:
                left = mid + 1
            else:
                right = mid
        if left == length_first_intervals:
            res_index = -1
        else:
            res_index = sorted_first_intervals[left][0]
        res.append(res_index)
    return res

# todo 双指针（莫队思想）
