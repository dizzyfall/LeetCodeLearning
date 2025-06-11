"""
@Project ：LeetCode 
@File    ：leetcode_528_3stars.py
@Author  ：DZY
@Date    ：2025/4/23 12:00 
"""
import random
from typing import List

"""
528. 按权重随机选择
给你一个 下标从 0 开始 的正整数数组 w ，其中 w[i] 代表第 i 个下标的权重。
请你实现一个函数 pickIndex ，它可以 随机地 从范围 [0, w.length - 1] 内（含 0 和 w.length - 1）选出并返回一个下标。选取下标 i 的 概率 为 w[i] / sum(w) 。
例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3) = 0.25 （即，25%），而选取下标 1 的概率为 3 / (1 + 3) = 0.75（即，75%）。
 
示例 1：
输入：
["Solution","pickIndex"]
[[[1]],[]]
输出：
[null,0]
解释：
Solution solution = new Solution([1]);
solution.pickIndex(); // 返回 0，因为数组中只有一个元素，所以唯一的选择是返回下标 0。

示例 2：
输入：
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
输出：
[null,1,1,1,1,0]
解释：
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // 返回 1，返回下标 1，返回该下标概率为 3/4 。
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 0，返回下标 0，返回该下标概率为 1/4 。
由于这是一个随机问题，允许多个答案，因此下列输出都可以被认为是正确的:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
诸若此类。

1 <= w.length <= 104
1 <= w[i] <= 105
pickIndex 将被调用不超过 104 次
"""

"""
思路：
这题描述很不清楚，看了好几遍都没懂什么意思，看了题解才大致明白

本质上就是概率，一种简单思路就是将概率拉成一条直线，把这直线上划分成多个部分，每一部分是一个概率
比如w=[3,1,2,4]，和为10，按照权重划分为|1，2，3|，|4|，|5，6|，|7，8，9，10|这四个部分，现在有一个随机数3，3在第一个部分，返回第一个部分的下标0
仔细看上面这个划分的4个部分，发现每个部分的左边界元素是前一部分出现元素个数+1，右边界元素是直到当前元素个数
再者，求w的前缀和为pre=[3,4,6,10]，任意一部分左边界元素是前一个部分+1，右边界是当前部分
即第i个区间，左：pre[i-1]+1，右：pre[i]
现在有一个随机数x，希望找到pre[i-1]+1<=x<=pre[i]
因此，而二分查找，找到大于等于x的最小下标i

"""


# 前缀和+二分法
class Solution:
    def __init__(self, w: List[int]):
        self.pre = []
        ans = 0
        for i in w:
            ans += i
            self.pre.append(ans)
        self.total = sum(w)

    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        left, right = 0, len(self.pre)
        while left < right:
            mid = left + (right - left) // 2
            if self.pre[mid] < x:
                left = mid + 1
            else:
                right = mid
        return left
