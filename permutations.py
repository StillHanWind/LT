"""
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = list()

        def fuc(ns, tmp):
            if not ns:
                result.append(tmp)
            for i in range(len(ns)):
                tm = tmp.copy()
                t = ns.copy()
                tm.append(t.pop(i))
                fuc(t, tm)

        fuc(nums, [])
        return result


def main():
    nums = [1, 2, 3]
    obj = Solution()
    print(obj.permute(nums))


if __name__ == '__main__':
    main()
