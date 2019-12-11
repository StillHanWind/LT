"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def func(s, r, l):
            if r == 0 and l == 0:
                res.append(s)
            if r > 0 and r > l:
                func(s+")", r-1, l)
            if l > 0:
                func(s+"(", r, l-1)
        res = []
        func("", n, n)
        return res


def main():
    n = 3
    s = Solution()
    print(s.generateParenthesis(n))


if __name__ == '__main__':
    main()
