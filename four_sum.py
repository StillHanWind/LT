"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        n = len(nums)
        nums.sort()
        result = list()
        for i in range(n-3):
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                lp = j+1
                rp = n-1
                while lp < rp:
                    if nums[i] + nums[j] + nums[lp] + nums[rp] == target:
                        result.append([nums[i], nums[j], nums[lp], nums[rp]])
                        while lp < rp and nums[lp] == nums[lp+1]:
                            lp += 1
                        while lp < rp and nums[rp] == nums[rp-1]:
                            rp -= 1
                    if nums[i] + nums[j] + nums[lp] + nums[rp] > target:
                        rp -= 1
                    else:
                        lp += 1
        return result


def main():
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    s = Solution()
    print(s.fourSum(nums, target))


if __name__ == '__main__':
    main()
