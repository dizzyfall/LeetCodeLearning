"""
@Project ：LeetCode 
@File    ：leetcode_31_4stars.py
@Author  ：DZY
@Date    ：2025/6/10 13:59 
"""

from typing import List

"""
31. 下一个排列
整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。
如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。
必须 原地 修改，只允许使用额外常数空间。

示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]

示例 3：
输入：nums = [1,1,5]
输出：[1,5,1]

提示：
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""


class Solution:

    # 根据思路第一次实现，写的不优美，可以优化
    def nextPermutation(self, nums: List[int]) -> None:
        # 找到较小数
        min_index = len(nums) - 2
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                min_index = i
                break
            min_index = -1
        # 根据上述代码逻辑，min_index要么是合法下标，要么是-1
        # 如果min_index=-1，说明序列是降序的，因此不需要找较大数，按照题目要求，只需最后升序排列就行
        # 因此需要判断
        if min_index >= 0:
            # 找到较大数
            for j in range(len(nums) - 1, min_index, -1):
                if nums[j] > nums[min_index]:
                    # 交换较小数和较大数
                    temp = nums[min_index]
                    nums[min_index] = nums[j]
                    nums[j] = temp
                    break

        # 较小数位置右边升序排序
        left, right = min_index + 1, len(nums) - 1
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

    # 优化
    def nextPermutation_one(self, nums: List[int]) -> None:
        # 找到较小数
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # 根据上述代码逻辑，min_index要么是合法下标，要么是-1
        # 如果min_index=-1，说明序列是降序的，因此不需要找较大数，按照题目要求，只需最后升序排列就行
        # 因此需要判断
        if i >= 0:
            # 找到较大数
            j = len(nums) - 1
            while j >= i and nums[j] <= nums[i]:
                j -= 1
            # 交换较小数和较大数
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        # 较小数位置右边升序排序
        left, right = i + 1, len(nums) - 1
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1


s = Solution()
nums = [4, 5, 2, 6, 3, 1]
s.nextPermutation(nums)
