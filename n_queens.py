"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        matrix = [['.' for _ in range(n)] for _ in range(n)]
        result = list()

        def func(t_matrix, c_row, count):
            if c_row == n and count == 0:
                result.append(''.join(t) for t in t_matrix)
            if (c_row == n and count > 0) or (c_row < n and count == 0):
                return
            for c_col in range(n):
                tag = True
                for row in range(c_row):
                    if row == c_row:
                        continue
                    for col in range(n):
                        if t_matrix[row][col] == 'Q' and (col == c_col or c_row - row == c_col - col or c_row - row == col - c_col):
                            tag = False
                    if not tag:
                        break
                if tag:
                    from copy import deepcopy
                    m = deepcopy(t_matrix)
                    m[c_row][c_col] = 'Q'
                    func(m, c_row+1, count-1)

        func(matrix, 0, n)
        return result


def main():
    n = 4
    obj = Solution()
    result = obj.solveNQueens(n)
    for i in result:
        for j in i:
            print(j)
        print()


if __name__ == '__main__':
    main()
