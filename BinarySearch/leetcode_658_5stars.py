"""
@Project ：LeetCode 
@File    ：leetcode_658_5stars.py
@Author  ：DZY
@Date    ：2025/4/18 14:20 
"""
from typing import List

"""
658. 找到 K 个最接近的元素
给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。
整数 a 比整数 b 更接近 x 需要满足：
|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b

示例 1：
输入：arr = [1,2,3,4,5], k = 4, x = 3
输出：[1,2,3,4]

示例 2：
输入：arr = [1,1,2,3,4,5], k = 4, x = -1
输出：[1,1,2,3]

1 <= k <= arr.length
1 <= arr.length <= 10^4
arr 按 升序 排列
-10^4 <= arr[i], x <= 10^4
"""


# 二分法+双指针
# 时间复杂度：O(logn+k)：二分查找需要 O(logn)，双指针查找需要 O(k)。
# 空间复杂度：O(1)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = self.find_min_idx(arr, x)
        left = right - 1
        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= len(arr) or x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        print(left)
        return arr[left + 1:right]

    def find_min_idx(self, arr: List[int], x: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        return left


s = Solution()
s.findClosestElements([1, 2, 3, 4, 5], 4, 3)
