"""
@Project ：LeetCode 
@File    ：leetcode_981.py
@Author  ：DZY
@Date    ：2025/4/11 16:14 
"""

"""
981. 基于时间的键值存储
设计一个基于时间的键值数据结构，该结构可以在不同时间戳存储对应同一个键的多个值，并针对特定时间戳检索键对应的值。
实现 TimeMap 类：
TimeMap() 初始化数据结构对象
void set(String key, String value, int timestamp) 存储给定时间戳 timestamp 时的键 key 和值 value。
String get(String key, int timestamp) 返回一个值，该值在之前调用了 set，其中 timestamp_prev <= timestamp 。如果有多个这样的值，它将返回与最大  timestamp_prev 关联的值。如果没有值，则返回空字符串（""）。

示例 1：
输入：
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

输出：
[null, null, "bar", "bar", null, "bar2", "bar2"]

解释：
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // 存储键 "foo" 和值 "bar" ，时间戳 timestamp = 1   
timeMap.get("foo", 1);         // 返回 "bar"
timeMap.get("foo", 3);         // 返回 "bar", 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"） 。
timeMap.set("foo", "bar2", 4); // 存储键 "foo" 和值 "bar2" ，时间戳 timestamp = 4  
timeMap.get("foo", 4);         // 返回 "bar2"
timeMap.get("foo", 5);         // 返回 "bar2"
"""


class TimeMap:

    def __init__(self):
        self.time_dict = {}
        # self.time_dict.append([])

    def set(self, key: str, value: str, timestamp: int) -> None:
        set_values = [key, value, timestamp]
        if key not in self.time_dict.keys():
            self.time_dict[key] = [set_values]
        else:
            self.time_dict[key].append(set_values)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_dict.keys():
            return ""
        time_list = self.time_dict[key]
        len_time_list = len(time_list)
        left, right = 0, len_time_list
        while left < right:
            mid = left + (right - left) // 2
            num = time_list[mid][2]
            if num <= timestamp:
                left = mid + 1
            else:
                right = mid
        if right == 0:
            return ""
        return time_list[left - 1][1]

# timemap=TimeMap()
# timemap.set("a","aaa",1)
# timemap.set("a","bbb",2)
# timemap.set("b","ccc",3)
# timemap.set("b","ddd",4)
# print(timemap.time_dict)
# todo hash表
