"""
@Project ：LeetCode 
@File    ：leetcode_611_4stars.py
@Author  ：DZY
@Date    ：2025/4/21 14:32 
"""
from typing import List

"""
611. 有效三角形的个数
给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。

示例 1:
输入: nums = [2,2,3,4]
输出: 3
解释:有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3

示例 2:
输入: nums = [4,2,3,4]
输出: 4

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""

"""
思路：

a+b>c
a+c>b
b+c>a

找到满足：a<=b<=c
则必定满足a+c>b和b+c>a
只需要满足a+b>c即可

循环枚举a和b，二分查找c，找到最大满足的c，使c<a+b，则当前c之前的元素都可以，将当前循环的答案累加
"""


# 排序+二分法
# 时间复杂度：O(n^2logn)：需要O(nlogn)进行排序，随后需要O(n^2logn)进行二分查。
# 空间复杂度：O(logn)：排序需要的栈空间。
def num_triangle(nums: List[int]) -> int:
    nums.sort()
    ans = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        for j in range(i + 1, len(nums)):
            if nums[j] == 0:
                continue
            left, right = j + 1, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < nums[i] + nums[j]:
                    left = mid + 1
                else:
                    right = mid
            ans += left - 1 - j
    return ans


# 排序+双指针
# 双指针枚举最小边a
# 时间复杂度：O(n^2)：需要O(nlogn)进行排序，随后需要 O(n^2)的时间使用一重循环枚举a的下标以及使用双指针维护b,c的下标。
# 空间复杂度：O(logn)
def num_triangle_second(nums: List[int]) -> int:
    nums.sort()
    ans = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        k = i
        for j in range(i + 1, len(nums)):
            if nums[i] == 0:
                continue
            while k + 1 < len(nums) and nums[k + 1] < nums[i] + nums[j]:
                k += 1
            ans += k - j
    return ans

# todo
# 双指针枚举最大边
