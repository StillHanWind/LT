"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
"""


class Solution1:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        count = 0
        sign = bool(dividend >= 0) ^ bool(divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            divisor <<= 1
            count += 1
        while count > 0:
            count -= 1
            divisor >>= 1
            if dividend >= divisor:
                dividend -= divisor
                result += 1 << count
        if sign:
            result = -result
        return result if -2**31 <= result <= 2**31-1 else 2**31-1


def main():
    dividend = 2 ** 32
    divisor = 2
    s = Solution1()
    print(s.divide(dividend, divisor))


if __name__ == '__main__':
    main()
