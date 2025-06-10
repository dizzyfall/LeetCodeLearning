"""
@Project ：LeetCode 
@File    ：leetcode_15_3stars.py
@Author  ：DZY
@Date    ：2025/5/12 14:28 
"""
from typing import List

"""
15. 三数之和
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。

示例 2：
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。

示例 3：
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
 
提示：
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

# 双指针
"""
思路：
一开始就想着使用双指针，题目又要求不重复，因此对数组进行排序
根据双指针的基本知识，必须固定一边，移动另一边
类似 有效三角形的个数问题（leetcode611），首先排序保证三元组a<=b<=c，使用循环固定a，使用双指针来找b和c，当固定b的时候，在下一个循环的b一定比之前的大，
为了保证a+b+c=0，则c一定比之前的c要小，因此b从小到大枚举，c从大到小枚举，是一个相向的双指针。
需要注意，对于每一个元素，需要判断当前值和上一次的值是否相同，保证不重复
"""


def threeSum(nums: List[int]) -> List[List[int]]:
    # 排序
    nums.sort()
    n = len(nums)
    ans = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            cur = nums[i] + nums[left] + nums[right]
            if cur == 0:
                ans.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif cur < 0:
                left += 1
            else:
                right -= 1
    return ans


# [-4,-1,-1,0,1,2]
ans = threeSum([-1, 0, 1, 2, -1, -4])
print(ans)
