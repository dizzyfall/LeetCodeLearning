"""
@Project ：LeetCode 
@File    ：leetcode_354_5stars.py
@Author  ：DZY
@Date    ：2025/4/28 10:54 
"""
from typing import List

"""
354. 俄罗斯套娃信封问题
给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
注意：不允许旋转信封。

示例 1：
输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

示例 2：
输入：envelopes = [[1,1],[1,1],[1,1]]
输出：1

1 <= envelopes.length <= 105
envelopes[i].length == 2
1 <= wi, hi <= 105
"""

"""
思路：
俄罗斯套娃信封问题很像最长递增子序列问题，对于最长递增子序列是一维数组，而俄罗斯套娃信封问题上升到二维数组
因此想法和之前的二分法或者双指针类似，能不能固定一个维度，只对另一个维度求解，这样能够降低二维的难度，转换为一维，也就是求最长递增子序列的问题

第一种思路就是先按w[i]升序，再按h[i]升序，这样保证w[i]是递增的，至少w[i]这边可以不用管了，再根据h[i]升序过后，求h[i]的最长递增子序列长度
这种思路有问题！题目并没有保证w[i]一定严格不相等，也就是说信封的宽度可能相等，在w[i]相等的情况下，按h[i]升序求最长递增子序列长度，得到的答案就是错的
因为题目要求更大的信封的宽度必须大于小的信封，而不能相等！

例如[1,8],[2,3],[5,2],[5,4]这几个信封，按照w[i]升序，再按h[i]升序，最后算h[i]的最长递增子序列是2，当这种情况下只存在一个信封，放不了任何其他信封

因此对于第一种思路，一个巧妙的优化是对h[i]升序改为h[i]降序，其他保持不变！这样当w[i]相等时，由于h[i]降序，最长递增子序列长度只有1，也就是最多选取一个信封，不会出现上述问题

先按w[i]升序，再按h[i]降序，很巧妙

求解最长递增子序列和leetcode_300一样，用动态规划，或者用动态规划+二分法进行优化
"""


# 先按w[i]升序，再按h[i]降序
# 动态规划
def max_envelopes_first_method(envelopes: List[List[int]]) -> int:
    sorted_envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
    num_envelopes = len(envelopes)
    dp = [1] * num_envelopes

    for i in range(num_envelopes):
        for j in range(i):
            if sorted_envelopes[j][1] < sorted_envelopes[i][1]:
                dp[i] = max(dp[j] + 1, dp[i])

    return max(dp)


# 动态规划+二分法
# https://leetcode.cn/problems/longest-increasing-subsequence/solutions/14796/dong-tai-gui-hua-she-ji-fang-fa-zhi-pai-you-xi-jia/
def max_envelopes_second_method(envelopes: List[List[int]]) -> int:
    pass
