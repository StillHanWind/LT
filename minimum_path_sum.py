"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i - 1 < 0 and j - 1 < 0:
                    continue
                elif i - 1 < 0 <= j - 1:
                    grid[i][j] += grid[i][j-1]
                elif i - 1 >= 0 > j - 1:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += grid[i-1][j] if grid[i-1][j] < grid[i][j-1] else grid[i][j-1]
        return grid[-1][-1]


def main():
    # grid = [
    #     [1, 3, 1],
    #     [1, 5, 1],
    #     [4, 2, 1]
    # ]
    grid = [
        [0, 1],
        [1, 0]
    ]
    obj = Solution()
    print(obj.minPathSum(grid))


if __name__ == '__main__':
    main()
