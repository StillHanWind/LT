"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""


class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ["" for _ in range(numRows)]
        f = 1
        n = 0
        for c in s:
            result[n] += c
            n += f
            if (n == numRows - 1 and f > 0) or (n == 0 and f < 0):
                f = -f
        return "".join(result)


def main():
    string = "a"
    s = Solution1()
    print(s.convert(string, 1))


if __name__ == '__main__':
    main()
