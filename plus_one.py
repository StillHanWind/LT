"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        plus = 1
        for i in range(n-1, -1, -1):
            digits[i] += plus
            plus = digits[i] // 10
            digits[i] %= 10
            if not plus:
                break
        if plus:
            digits = [plus] + digits
        return digits


def main():
    digits = []
    obj = Solution()
    print(obj.plusOne(digits))


if __name__ == '__main__':
    main()