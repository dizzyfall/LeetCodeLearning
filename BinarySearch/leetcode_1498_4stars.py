"""
@Project ：LeetCode 
@File    ：leetcode_1498_4stars.py
@Author  ：DZY
@Date    ：2025/4/22 13:01 
"""
import math
from typing import List

"""
1498. 满足条件的子序列数目
给你一个整数数组 nums 和一个整数 target 。
请你统计并返回 nums 中能满足其最小元素与最大元素的 和 小于或等于 target 的 非空 子序列的数目。
由于答案可能很大，请将结果对 109 + 7 取余后返回。

示例 1：
输入：nums = [3,5,6,7], target = 9
输出：4
解释：有 4 个子序列满足该条件。
[3] -> 最小元素 + 最大元素 <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

示例 2：
输入：nums = [3,3,6,8], target = 10
输出：6
解释：有 6 个子序列满足该条件。（nums 中可以有重复数字）
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

示例 3：
输入：nums = [2,3,3,4,6,7], target = 12
输出：61
解释：共有 63 个非空子序列，其中 2 个不满足条件（[6,7], [7]）
有效序列总数为（63 - 2 = 61）
 
1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= target <= 106
"""

"""
思路：
固定住子序列的最小值min，那这个子序列的最大值max一定小于等于target-min
因此有：min<=max<=target-min
则：2min<=target -> min<=target//2

设max=target-min
二分查找小于等于max，则答案为2^(max_index-min_index) ->
最大的都满足，则比最大的小的都满足，然后序列并不要求连续，则每个符合的元素都可以选择或者不选择两种情况，排列组合或者乘法原理可以求出答案

其中有个小技巧，最后答案很大需要取余，但是我一开始实现的得到答案最后取余，但是好像会溢出，导致答案不对
因此根据(a+b)%p=[(a%p)+(b%p)]%p来预处理每一次循环的答案，这样就不会出错了！！！
"""


# 预处理！！！，不然答案过大会溢出，导致答案错误
def num_sub_seq(nums: List[int], target: int) -> int:
    # 预处理
    n = len(nums)
    P = int(math.pow(10, 9) + 7)
    f = [1] + [0] * (n - 1)
    for i in range(1, n):
        f[i] = f[i - 1] * 2 % P

    # 二分
    nums.sort()
    ans = 0
    for i in range(len(nums)):
        if 2 * nums[i] > target:
            break
        max = target - nums[i]
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= max:
                left = mid + 1
            else:
                right = mid
        # print(left,i)
        if left - 1 < i:
            pass
        else:
            ans += f[left - 1 - i]
        # print(ans % p)
    return ans % P


num_sub_seq(
    [6, 10, 12, 3, 29, 21, 12, 25, 17, 19, 16, 1, 2, 24, 9, 17, 25, 22, 12, 22, 26, 24, 24, 11, 3, 7, 24, 5, 15, 30, 23,
     5, 20, 10, 19, 20, 9, 27, 11, 4, 23, 4, 4, 12, 22, 27, 16, 11, 26, 10, 23, 26, 16, 21, 24, 21, 17, 13, 21, 9, 16,
     17, 27], 26)

# 这种做法好像有问题，就是当ans比较大的时候，最后再取余数好像会溢出，因此需要一开始就取余
# 上面这个例子好像就溢出了
# def num_sub_seq(nums: List[int], target: int) -> int:
#     nums.sort()
#     ans=0
#     for i in range(len(nums)):
#         if 2*nums[i]>target:
#             break
#         max=target-nums[i]
#         left,right=0,len(nums)
#         while left<right:
#             mid=left+(right-left)//2
#             if nums[mid]<=max:
#                 left=mid+1
#             else:
#                 right=mid
#         if left-1<i:
#             pass
#         else:
#             ans+=math.pow(2,left-1-i)
#     return int(ans%(math.pow(10,9)+7))
