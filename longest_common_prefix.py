"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        mi = len(strs[0])
        for s in strs:
            if len(s) < mi:
                mi = len(s)
        for i in range(mi):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return strs[0][:i]
        return strs[0][:mi]


def main():
    strs = []
    s = Solution()
    print(s.longestCommonPrefix(strs))


if __name__ == '__main__':
    main()
