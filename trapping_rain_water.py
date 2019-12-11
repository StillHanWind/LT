"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        ml = [0]*n
        mr = [0]*n
        ml[0] = height[0]
        mr[-1] = height[-1]
        for i in range(1, n):
            ml[i] = max(height[i], ml[i-1])
        for i in range(n-2, -1, -1):
            mr[i] = max([height[i], mr[i+1]])
        result = 0
        for i in range(n):
            result += min(ml[i], mr[i]) - height[i]
        return result


def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    obj = Solution()
    print(obj.trap(height))


if __name__ == '__main__':
    main()
