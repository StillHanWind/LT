"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        candidates.sort()

        def traceback(result_tmp, target_tmp, begin):
            if target_tmp == 0:
                result.append(result_tmp)
            if target_tmp < candidates[0]:
                return False
            for i in range(begin, len(candidates)):
                if i > begin and candidates[i] == candidates[i-1]:
                    continue
                if target_tmp >= candidates[i]:
                    traceback(result_tmp+[candidates[i]], target_tmp-candidates[i], i+1)
                else:
                    break

        traceback([], target, 0)
        return result


def main():
    candidates = [2, 5, 2, 1, 2]
    target = 5
    obj = Solution()
    print(obj.combinationSum2(candidates, target))


if __name__ == '__main__':
    main()
