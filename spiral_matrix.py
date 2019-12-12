"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        result = list()

        def func(begin, end):
            if len(result) == m*n or begin[0] > end[0] or begin[1] > end[1]:
                return

            for i in range(begin[1], end[1]+1):
                result.append(matrix[begin[0]][i])

            for i in range(begin[0]+1, end[0]+1):
                result.append(matrix[i][end[1]])

            if end[0]-begin[0] > 0:
                for i in range(end[1]-1, begin[1]-1, -1):
                    result.append(matrix[end[0]][i])

            if end[0]-begin[0]>1 and end[1]-begin[1]>0:
                for i in range(end[0]-1, begin[0], -1):
                    result.append(matrix[i][begin[1]])

            func((begin[0]+1, begin[1]+1), (end[0]-1, end[1]-1))

        func((0, 0), (m-1, n-1))
        return result


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    matrix = [
        [1]
    ]
    obj = Solution()
    print(obj.spiralOrder(matrix))


if __name__ == '__main__':
    main()
