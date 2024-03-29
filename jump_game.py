"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index, n = 0, len(nums)
        while index < n - 1:
            if nums[index] == 0:
                return False
            mx = 0
            for j in [(i + nums[i] if i < n - 1 else 1, i) for i in range(index, index + nums[index] + 1)]:
                if j[1] >= n - 1:
                    index = j[1]
                    break
                if j[0] >= mx:
                    mx, index = j[0], j[1]
        return True


def main():
    nums = [0]
    obj = Solution()
    print(obj.canJump(nums))


if __name__ == '__main__':
    main()
