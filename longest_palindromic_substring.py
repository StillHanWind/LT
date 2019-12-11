"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution1:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        result = ""

        def judge(prefix, suffix):
            nonlocal result
            temp = ""
            while prefix >= 0 and suffix < len(s) and s[prefix] == s[suffix]:
                if prefix == suffix:
                    temp = s[prefix]
                else:
                    temp = s[prefix] + temp + s[suffix]
                prefix -= 1
                suffix += 1
            result = temp if len(temp) > len(result) else result

        for i in range(len(s)*2-1):
            if i % 2 == 0:
                a = z = i // 2 - 1
                judge(a, z)
            else:
                a = i // 2
                z = i // 2 + 1
                judge(a, z)
        return result


def main():
    string = "c"
    s = Solution1()
    print(s.longestPalindrome(string))


if __name__ == '__main__':
    main()
