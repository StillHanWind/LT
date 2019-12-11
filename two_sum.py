"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution1:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            t = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == t:
                    return [i, j]
        return []


class Solution2:
    def twoSum(self, nums, target):
        d = {k: v for v, k in enumerate(nums)}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in d and d[t] != i:
                return [i, d[t]]
        return []


class Solution3:
    def twoSum(self, nums, target):
        d = dict()
        for i in range(len(nums)):
            t = target - nums[i]
            if t in d:
                return [d[t], i]
            d[nums[i]] = i
        return []


def main():
    nums = [2, 7, 11, 15]
    target = 26
    s = Solution3()
    result = s.twoSum(nums=nums, target=target)
    print(result)


if __name__ == '__main__':
    main()
