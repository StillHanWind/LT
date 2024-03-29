"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def searchR(lp, rp):
            if lp > rp:
                return -1
            mid = (lp + rp) // 2
            if nums[mid] == target and nums[mid-1] < target:
                return mid
            elif nums[mid] < target:
                return searchR(mid+1, rp)
            else:
                return searchR(lp, mid-1)

        def searchL(lp, rp):
            if lp > rp:
                return -1
            mid = (lp + rp) // 2
            if nums[mid] == target and nums[mid+1] > target:
                return mid
            elif nums[mid] <= target:
                return searchL(mid+1, rp)
            else:
                return searchL(lp, mid-1)

        lb = 0
        rb = len(nums)-1
        if nums[lb] == target:
            sr = lb
        else:
            sr = searchR(lb, rb)
        if nums[rb] == target:
            sl = rb
        else:
            sl = searchL(lb, rb)
        return [sr, sl]


def main():
    nums = [5]
    target = 5
    obj = Solution()
    print(obj.searchRange(nums, target))


if __name__ == '__main__':
    main()
