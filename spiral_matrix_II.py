"""
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        result = [[0 for _ in range(n)] for _ in range(n)]
        nums = [i for i in range(1, n*n+1)]
        index = 0

        def func(begin, end):
            nonlocal index
            if index == len(nums):
                return

            for i in range(begin[1], end[1] + 1):
                result[begin[0]][i] = nums[index]
                index += 1

            for i in range(begin[0] + 1, end[0] + 1):
                result[i][end[1]] = nums[index]
                index += 1

            if end[0] - begin[0] > 0:
                for i in range(end[1] - 1, begin[1] - 1, -1):
                    result[end[0]][i] = nums[index]
                    index += 1

            if end[0] - begin[0] > 1 and end[1] - begin[1] > 0:
                for i in range(end[0] - 1, begin[0], -1):
                    result[i][begin[1]] = nums[index]
                    index += 1

            func((begin[0] + 1, begin[1] + 1), (end[0] - 1, end[1] - 1))

        func((0, 0), (n - 1, n - 1))
        return result


def main():
    n = 3
    obj = Solution()
    result = obj.generateMatrix(n)
    for i in result:
        print(i)


if __name__ == '__main__':
    main()
