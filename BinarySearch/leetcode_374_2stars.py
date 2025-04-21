"""
@Project ：LeetCode 
@File    ：leetcode_374_2stars.py
@Author  ：DZY
@Date    ：2025/4/14 20:44 
"""

"""
374. 猜数字大小
我们正在玩猜数字游戏。猜数字游戏的规则如下：
我会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
如果你猜错了，我会告诉你，我选出的数字比你猜测的数字大了还是小了。

你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有三种可能的情况：
-1：你猜的数字比我选出的数字大 （即 num > pick）。
1：你猜的数字比我选出的数字小 （即 num < pick）。
0：你猜的数字与我选出的数字相等。（即 num == pick）。

注意！！！
1 <= n <= 2^31 - 1
1 <= pick <= n
"""


def guess(num: int) -> bool:
    pass


# 我这样做首先生成了一个从1-n的数组，完全是多余的，这样做肯定会超内存
# 自己思维又固定了
def guess_number_false(n: int) -> int:
    nums = [i for i in range(1, n + 2)]
    print(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        num = nums[mid]
        ans = guess(mid)
        if ans == 0:
            return num
        elif ans == -1:
            right = mid - 1
        else:
            left = mid + 1


# left和right就代表数字就行了，不需要指向数字的下标
def guess_number_true(n: int) -> int:
    left, right = 1, n
    while left <= right:
        mid = left + (right - left) // 2
        ans = guess(mid)
        if ans == 0:
            return mid
        elif ans == -1:
            right = mid - 1
        else:
            left = mid + 1
