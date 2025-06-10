"""
@Project ：LeetCode 
@File    ：leetcode_19.py
@Author  ：DZY
@Date    ：2025/6/9 12:33 
"""

from typing import Optional

"""
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]
 
提示：
链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方法一：常规操作，计算链表长度，得到待删除结点的前一个节点，将其指向待删除节点的后面一个节点即可
class Solution:
    def _get_length(self, head):
        length = 0
        while head.next:
            length += 1
            head = head.next
        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode(0, head)
        length = self._get_length(head)
        cur = head
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return head.next


# 方法二：双指针，或者是快慢指针
# 方法一首先需要计算链表长度，双指针不需要，但其思路还是找到待删除节点的前一个节点
# 使用同向双指针，使其间隔n个，这样遍历到最后，其中一个指针正好指向到待删除节点的前一个节点
# 输入：head = [-,1,2,3,4,5], n = 2
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    first = head
    big_head = ListNode(0, head)
    second = big_head
    for i in range(n):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return big_head.next
