"""
@Project ：LeetCode 
@File    ：leetcode_540_4stars.py
@Author  ：DZY
@Date    ：2025/4/17 19:00 
"""
from typing import List

"""
540. 有序数组中的单一元素
给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
请你找出并返回只出现一次的那个数。
你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。

示例 1:
输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2

示例 2:
输入: nums =  [3,3,7,7,10,11,11]
输出: 10
 
1 <= nums.length <= 105
0 <= nums[i] <= 105
"""


# 这是一种更通用的解法
# 官方题解并不是这样做的，但是官方题解只适用于元素出现两次->nums[mid] != nums[mid ^ 1]
# 如果元素出现多次，好像就不行了，这种解法根据一般性
def single_element(nums: List[int]) -> int:
    left, right = 0, len(nums) // 2
    while left < right:
        mid = left + (right - left) // 2
        if nums[2 * mid] != nums[2 * mid + 1]:
            right = mid
        else:
            left = mid + 1
    return nums[2 * left]


# 官方题解
def single_element_official(nums: List[int]) -> int:
    pass

# 假如题目改为每个元素出现3次、四次，或者n次呢，怎么做？？？
# 上述方法可以解决
# 时间复杂度为 O(log(n/m))，m是元素出现的次数
