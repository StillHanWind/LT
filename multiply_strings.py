"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0" or not num1 or not num2:
            return "0"
        if len(num2) > len(num1):
            num1, num2 = num2, num1

        l1, l2 = len(num1), len(num2)
        product = 0
        for i2 in range(l2):
            tmp_product = 0
            for i1 in range(l1):
                tmp_product = tmp_product*10 + int(num1[i1]) * int(num2[i2])
            product = product*10 + tmp_product
        return str(product)


def main():
    num1 = "123"
    num2 = "456"
    obj = Solution()
    print(obj.multiply(num1, num2))


if __name__ == '__main__':
    main()
