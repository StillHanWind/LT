"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        le = 0
        for i in range(len(s)):
            t = {s[i]}
            for j in range(i+1, len(s)):
                if s[j] not in t:
                    t.add(s[j])
                else:
                    break
            if len(t) > le:
                le = len(t)
        return le


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        t = set()
        le = i = j = 0
        while i < n and j < n:
            if s[j] not in t:
                t.add(s[j])
                j += 1
                le = le if le > j-i else j-i
            else:
                t.remove(s[i])
                i += 1
        return le


class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        le = 0
        m = dict()
        for j in range(len(s)):
            if s[j] in m:
                if m[s[j]] > i:
                    i = m[s[j]]
            if j-i+1 > le:
                le = j-i+1
            m[s[j]] = j+1
        return le


def main():
    string = "pwwkew"
    s = Solution3()
    result = s.lengthOfLongestSubstring(string)
    print(result)


if __name__ == '__main__':
    main()
