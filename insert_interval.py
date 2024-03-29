"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                intervals = intervals[:i]+[newInterval]+intervals[i:]
        if intervals[-1][0] < newInterval[0]:
            intervals.append(newInterval)
        index = 1
        while index < len(intervals):
            if intervals[index - 1][1] < intervals[index][0]:
                index += 1
            elif intervals[index - 1][1] >= intervals[index][1]:
                intervals.pop(index)
            else:
                intervals[index - 1][1] = intervals[index][1]
        return intervals


def main():
    intervals = [[1, 5]]
    newInterval = [2, 7]
    obj = Solution()
    print(obj.insert(intervals, newInterval))


if __name__ == '__main__':
    main()
