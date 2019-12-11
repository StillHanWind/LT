"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        elif nums[0] == target:
            return 0
        elif len(nums) == 1 and nums[0] != target:
            return -1

        def find_rotated_point(l, r):
            rotate_index = (l+r)//2
            if nums[rotate_index-1] > nums[rotate_index]:
                return rotate_index
            elif nums[rotate_index] > nums[r]:
                l = rotate_index+1
            else:
                r = rotate_index-1
            return find_rotated_point(l, r)

        lb = 0
        rb = len(nums)-1
        rotate_i = find_rotated_point(lb, rb)

        def find_target(l, r):
            if l > r:
                return -1
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return find_target(mid+1, r)
            else:
                return find_target(l, mid-1)

        if target > nums[rb]:
            return find_target(lb, rotate_i-1)
        else:
            return find_target(rotate_i, rb)


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    obj = Solution()
    print(obj.search(nums, target))


if __name__ == '__main__':
    main()
