"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, value in enumerate(nums):
            if value == target:
                return index
            if value > target:
                nums.insert(index, target)
                return index
        nums.append(target)
        return len(nums)-1


def main():
    nums = [1, 3, 5, 6]
    target = 0
    s = Solution()
    print(s.searchInsert(nums, target))


if __name__ == '__main__':
    main()
