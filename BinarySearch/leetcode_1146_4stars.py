"""
@Project ：LeetCode 
@File    ：leetcode_1146_4stars.py
@Author  ：DZY
@Date    ：2025/4/11 17:19 
"""

"""
1146. 快照数组
实现支持下列接口的「快照数组」- SnapshotArray：
SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
void set(index, val) - 会将指定索引 index 处的元素设置为 val。
int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。

示例：
输入：["SnapshotArray","set","snap","set","get"]
     [[3],[0,5],[],[0,6],[0,0]]
     
输出：[null,null,0,null,5]

解释：
SnapshotArray snapshotArr = new SnapshotArray(3); // 初始化一个长度为 3 的快照数组
snapshotArr.set(0,5);  // 令 array[0] = 5
snapshotArr.snap();  // 获取快照，返回 snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5
"""


class SnapshotArray:

    def __init__(self, length: int):
        self.count_snap = 0
        self.array = [[] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.count_snap, val])

    def snap(self) -> int:
        self.count_snap += 1
        return self.count_snap - 1

    def get(self, index: int, snap_id: int) -> int:
        left, right = 0, len(self.array[index])
        while left < right:
            mid = left + (right - left) // 2
            num = self.array[index][mid][0]
            if num <= snap_id:
                left = mid + 1
            else:
                right = mid
        if left == 0:
            return 0
        return self.array[index][left - 1][1]


# s=SnapshotArray(1)
# s.set(0,4)
# s.snap()
# print(s.get(0,0))

s = SnapshotArray(4)
s.snap()
s.snap()
print(s.get(3, 1))
