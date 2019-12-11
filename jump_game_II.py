"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。
"""

from typing import List


class Solution1:
    def jump(self, nums: List[int]) -> int:
        result = list()
        if len(nums) == 1:
            return 0

        def dp(ns, jp):
            if jp > len(nums):
                return
            n = len(ns)
            for i in range(n-2, -1, -1):
                if ns[i] >= n-1 - i:
                    if i == 0:
                        result.append(jp+1)
                    dp(ns[:i+1], jp+1)

        dp(nums, 0)
        return min(result)


class Solution2:
    def jump(self, nums: List[int]) -> int:
        index, result, n = 0, 0, len(nums)
        while index < n-1:
            mx = 0
            for j in [(i+nums[i] if i < n-1 else 1, i) for i in range(index, index+nums[index]+1)]:
                if j[1] >= n-1:
                    index = j[1]
                    break
                if j[0] >= mx:
                    mx, index = j[0], j[1]
            result += 1
        return result


def main():
    nums = [2, 3, 1]
    obj = Solution2()
    print(obj.jump(nums))


if __name__ == '__main__':
    main()
