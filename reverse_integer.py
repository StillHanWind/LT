"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution1:
    def reverse(self, x: int) -> int:
        x = str(x)
        tag = x[0] if x[0] == '-' else ''
        x = x if x[0] != '-' else x[1:]
        x = ''.join(reversed(x))
        if len(x) > 1:
            x.rstrip('0')
        x = int(tag + x)
        x = x if -2147483648 <= x <= 2147483647 else 0
        return x


class Solution2:
    def reverse(self, x: int) -> int:
        result = 0
        f = False
        if x < 0:
            x = -x
            f = True
        while x:
            pop = x % 10
            print(pop)
            x //= 10
            result = result * 10 + pop
        if f:
            result = -result
        return result if -2147483648 <= result <= 2147483647 else 0


def main():
    i = -123
    s = Solution2()
    print(s.reverse(i))


if __name__ == '__main__':
    main()
