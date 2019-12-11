"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""


class Solution1:
    def findMedianSortedArrays(self, nums1, nums2):
        i = j = 0
        t = list()
        while i <= len(nums1) and j <= len(nums2):
            if i == len(nums1):
                t += nums2[j:]
                break
            elif j == len(nums2):
                t += nums1[i:]
                break
            if nums1[i] <= nums2[j]:
                t.append(nums1[i])
                i += 1
            else:
                t.append(nums2[j])
                j += 1
        n = len(t)
        if n == 1:
            return t[0]
        if n == 2:
            return (t[0]+t[1])/2
        if ((n-1)/2) % ((n-1)//2) != 0:
            result = (t[(n-1)//2] + t[(n-1)//2 + 1])/2
        else:
            result = t[(n-1)//2]
        return result


def main():
    nums1 = [0]
    nums2 = [2, 3]
    s = Solution1()
    result = s.findMedianSortedArrays(nums1, nums2)
    print(result)


if __name__ == '__main__':
    main()
