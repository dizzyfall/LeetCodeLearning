"""
@Project ：LeetCode 
@File    ：leetcode_26_2stars.py
@Author  ：DZY
@Date    ：2025/6/9 13:37 
"""

from typing import List

"""
26. 删除有序数组中的重复项
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：
更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。

示例 1：
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
 
提示：
1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums 已按 非严格递增 排列
"""


# 双指针
# 更详细的来说，是同向双指针，或者说是快慢指针
class Solution:
    # 快指针用来筛选重复元素，慢指针定位原数组位置，用来修改原数组元素
    def removeDuplicates(self, nums: List[int]):
        first, second = 1, 1
        while second < len(nums):
            if nums[second] != nums[second - 1]:
                nums[first] = nums[second]
                first += 1
            second += 1
        return first

    # 自己一开始思考的写法，也是快慢指针，不过没有考虑原地删除nums，而是重新创建一个结果数组
    # 这里两个指针含义和第一种写法不同。这两个指针作用都是用来筛选重复元素，和第一种方法的两个指针作用不同
    def removeDuplicates_one(self, nums: List[int]):
        first, second = 0, 0
        res = []
        while second < len(nums):
            if second == first and second == len(nums) - 1:
                res.append(nums[first])
                break
            if nums[first] == nums[second]:
                second += 1
            else:
                res.append(nums[first])
                first = second
        return len(res)


s = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
res = s.removeDuplicates(nums)
print(res)
