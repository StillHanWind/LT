"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

from typing import List


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = list()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        r = sorted([nums[i], nums[j], nums[k]])
                        if r not in result:
                            result.append(r)
        return result


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        result = list()
        for i in range(len(nums)):
            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lp = i + 1
            rp = len(nums) - 1
            while lp < rp:
                if nums[i] + nums[lp] + nums[rp] == 0:
                    result.append([nums[i], nums[lp], nums[rp]])
                    while lp < rp and nums[lp] == nums[lp + 1]:
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp - 1]:
                        rp -= 1
                    lp += 1
                    rp -= 1
                elif nums[i] + nums[lp] + nums[rp] > 0:
                    rp -= 1
                else:
                    lp += 1
        return result


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution2()
    print(s.threeSum(nums))


if __name__ == '__main__':
    main()
