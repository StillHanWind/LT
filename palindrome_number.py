"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if 0 <= x < 10:
            return True
        n_list = list()
        while x != 0:
            r = x % 10
            x //= 10
            n_list.append(r)
        r_list = list(reversed(n_list))
        return True if r_list == n_list else False


def main():
    i = 121
    s = Solution()
    print(s.isPalindrome(i))


if __name__ == '__main__':
    main()
