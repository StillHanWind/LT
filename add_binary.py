"""
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [c for c in a]
        b = [c for c in b]
        a.reverse()
        b.reverse()
        la = len(a)
        lb = len(b)
        result = list()
        carry = 0
        for i in range(la if la > lb else lb):
            sum = (int(a[i]) if i < la else 0) + (int(b[i]) if i < lb else 0) + carry
            result.append(str(sum % 2))
            carry = sum // 2
        if carry:
            result.append(str(carry))
        result.reverse()
        return "".join(result)


def main():
    a = "11"
    b = "1"
    obj = Solution()
    print(obj.addBinary(a, b))


if __name__ == '__main__':
    main()
