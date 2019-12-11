"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = list()
        nums.sort()

        def fuc(ns, tmp):
            if len(ns) == 0:
                result.append(tmp)
                return
            tm = tmp.copy()
            t = ns.copy()
            tm.append(t.pop(0))
            fuc(t, tm)
            for i in range(1, len(ns)):
                if ns[i] == ns[i-1]:
                    continue
                tm = tmp.copy()
                t = ns.copy()
                tm.append(t.pop(i))
                fuc(t, tm)

        fuc(nums, [])
        return result


def main():
    nums = [1, 1, 2]
    obj = Solution()
    print(obj.permuteUnique(nums))


if __name__ == '__main__':
    main()