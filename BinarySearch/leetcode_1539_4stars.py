"""
@Project ：LeetCode 
@File    ：leetcode_1539_4stars.py
@Author  ：DZY
@Date    ：2025/4/15 19:32 
"""
from typing import List

"""
1539. 第 k 个缺失的正整数
给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。
请你找到这个数组里第 k 个缺失的正整数。

示例 1：
输入：arr = [2,3,4,7,11], k = 5
输出：9
解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。

示例 2：
输入：arr = [1,2,3,4], k = 2
输出：6
解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
"""


# arr = [2,3,4,7,11], k = 5
# arr中每个元素对应的缺失元素数组：[1,1,1,3,6]->怎么算出来的：arr[i]-i-1
def find_kth_positive(arr: List[int], k: int) -> int:
    # 这种写法和下面一种主要是返回的缺失值计算方法不同
    # 这种是官方或者大部分的写法
    # 但是我感觉不严谨：“num-mid-1<k”，得到的left是大于等于，left-1是小于，忽略了等于的情况，但是最后的缺失值计算方式中等于情况也适用
    # left,right=0,len(arr)
    # while left<right:
    #     mid=left+(right-left)//2
    #     num=arr[mid]
    #     if num-mid-1<k:
    #         left=mid+1
    #     else:
    #         right=mid
    # return  k-(arr[left-1]-(left-1)-1)+arr[left-1]

    # 这种是我自己按照left是大于等于情况讨论的
    # 可以看到当“left==len(arr)”时，缺失值计算方式还是和第一种一样，但是分开写更清楚一些
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        num = arr[mid]
        if num - mid - 1 < k:
            left = mid + 1
        else:
            right = mid
    if left == len(arr):
        return (k - (arr[left - 1] - (left - 1) - 1)) + arr[left - 1]
    return arr[left] - ((arr[left] - left - 1) - k) - 1


print(find_kth_positive([5, 6, 7, 8, 9], 9))

# 总结
# 1.原数组中每个元素的缺失值个数怎么计算的
# 2.二分法分的是哪个变量
# 3.最后缺失的数是怎么计算的
