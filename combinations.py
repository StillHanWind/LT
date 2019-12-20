"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # if n == k:
        #     return [[i for i in range(1, n+1)]]
        nums = [i for i in range(1, n+1)]
        result = list()

        def func(t_nums, t_result, tk):
            if len(t_result) == k:
                result.append(t_result)
                return
            for index, i in enumerate(t_nums):
                if len(t_nums) - tk < index:
                    return
                t_result_l = t_result[:]
                t_result_l.append(i)
                func(t_nums[index+1:], t_result_l, tk-1)

        func(nums, [], k)
        return result


def main():
    n = 3
    k = 3
    obj = Solution()
    print(obj.combine(n, k))


if __name__ == '__main__':
    main()
