"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""

from typing import List


class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0]*3
        for n in nums:
            counts[n] += 1
        index = 0
        for num, count in enumerate(counts):
            for _ in range(count):
                nums[index] = num
                index += 1


class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        begin, end, cur = 0, n-1, 0
        while cur <= end:
            if nums[cur] == 0:
                nums[begin], nums[cur] = nums[cur], nums[begin]
                begin += 1
                cur += 1
            elif nums[cur] == 2:
                nums[end], nums[cur] = nums[cur], nums[end]
                end -= 1
            elif nums[cur] == 1:
                cur += 1


def main():
    nums = [2, 0, 1]
    obj = Solution2()
    obj.sortColors(nums)
    print(nums)


if __name__ == '__main__':
    main()
