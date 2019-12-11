"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3:
            return 0
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        lz = abs(nums[0] + nums[1] + nums[2] - target)
        for i in range(len(nums)):
            lp = i + 1
            rp = len(nums) - 1
            while lp < rp:
                sums = nums[i] + nums[lp] + nums[rp]
                a = abs(sums-target)
                if a < lz:
                    result, lz = sums, a
                if nums[i] + nums[lp] + nums[rp] < target:
                    lp += 1
                elif nums[i] + nums[lp] + nums[rp] > target:
                    rp -= 1
                else:
                    return target
        return result


def main():
    nums = [0, 2, 1, -3]
    target = 1
    s = Solution()
    print(s.threeSumClosest(nums, target))


if __name__ == '__main__':
    main()
