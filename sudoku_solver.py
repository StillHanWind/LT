"""
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。



一个数独。



答案被标成红色。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
"""

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set(i for i in range(1, 10)) for _ in range(9)]
        cols = [set(i for i in range(1, 10)) for _ in range(9)]
        blocks = [set(i for i in range(1, 10)) for _ in range(9)]

        empty = list()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].remove(int(board[i][j]))
                    cols[j].remove(int(board[i][j]))
                    blocks[(i//3)*3+j//3].remove(int(board[i][j]))
                else:
                    empty.append((i, j))

        def backtrace(itern):
            if itern == len(empty):
                return True
            i, j = empty[itern]
            b = (i//3)*3+j//3
            for v in rows[i] & cols[j] & blocks[b]:
                rows[i].remove(v)
                cols[j].remove(v)
                blocks[(i // 3) * 3 + j // 3].remove(v)
                board[i][j] = str(v)
                if backtrace(itern+1):
                    return True
                rows[i].add(v)
                cols[j].add(v)
                blocks[b].add(v)
            return False

        backtrace(0)


def main():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    obj = Solution()
    obj.solveSudoku(board)
    for i in board:
        print(i)


if __name__ == '__main__':
    main()
