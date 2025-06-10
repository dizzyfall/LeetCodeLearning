"""
@Project ：LeetCode 
@File    ：leetcode_27.py
@Author  ：DZY
@Date    ：2025/6/9 15:29 
"""
from typing import List

"""
27. 移除元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。
假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：
更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
返回 k。


示例 1：
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2,_,_]
解释：你的函数函数应该返回 k = 2, 并且 nums 中的前两个元素均为 2。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。

示例 2：
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3,_,_,_]
解释：你的函数应该返回 k = 5，并且 nums 中的前五个元素为 0,0,1,3,4。
注意这五个元素可以任意顺序返回。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。

 
提示：
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""


class Solution:
    # 方法一：类似leetcode_26，同向双指针，快指针用于判断是否和val相等，慢指针用于确定原数组位置
    # 这个方法有一个缺点：等于val的元素会重复的赋值给nums，因此可以继续优化

    def removeElement(self, nums: List[int], val: int) -> int:
        first = 0
        for second in range(len(nums)):
            if nums[second] != val:
                nums[first] = nums[second]
                first += 1
        return first

    # 方法二：优化，相向双指针
    # 注意到题目说返回顺序是任意的，并不需要按照原nums数组顺序返回
    # 因此对于原数组第一个元素，如果这个元素等于val，可以将原数组最后一个元素赋值过来，并且扔掉最后一个元素（指针初始化指向最后一个元素，指针向前移动）。
    # 如果赋值过来的元素仍然等于val，那再把新的最后一个元素赋值过去（指针指向的倒数第二个元素），如此往复。
    def removeElement_one(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1
        return left


s = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
res = s.removeElement_one(nums, 2)
print(res)
