"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        stack = [-1]
        for k in range(len(s)):
            if s[k] == '(':
                stack.append(k)
            else:
                stack.pop()
                if stack:
                    maxans = max(maxans, k - stack[-1])
                else:
                    stack.append(k)
        return maxans


def main():
    string = "(()"
    obj = Solution()
    print(obj.longestValidParentheses(string))


if __name__ == '__main__':
    main()
