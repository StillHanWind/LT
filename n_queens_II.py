"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        matrix = [['.' for _ in range(n)] for _ in range(n)]
        result = 0

        def func(t_matrix, c_row, count):
            if c_row == n and count == 0:
                nonlocal result
                result += 1
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
    n = 10
    obj = Solution()
    print(obj.totalNQueens(n))


if __name__ == '__main__':
    main()
