"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        candidates.sort()

        def traceback(result_tmp, target_tmp, begin):
            if target_tmp == 0:
                result.append(result_tmp)
            if target_tmp < candidates[0]:
                return False
            for i in range(begin, len(candidates)):
                if target_tmp >= candidates[i]:
                    traceback(result_tmp+[candidates[i]], target_tmp-candidates[i], i)
                else:
                    break

        traceback([], target, 0)
        return result


def main():
    candidates = [2, 3, 6, 7]
    target = 7
    obj = Solution()
    print(obj.combinationSum(candidates, target))


if __name__ == '__main__':
    main()
