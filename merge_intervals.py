"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        index = 1
        while index < len(intervals):
            if intervals[index-1][1] < intervals[index][0]:
                index += 1
            elif intervals[index-1][1] >= intervals[index][1]:
                intervals.pop(index)
            else:
                intervals[index-1][1] = intervals[index][1]
        return intervals


def main():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = [[1, 4], [4, 5]]
    obj = Solution()
    print(obj.merge(intervals))


if __name__ == '__main__':
    main()
