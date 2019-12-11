"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        strs = [d[c] for c in digits]
        if len(strs) < 1:
            return []
        result = [c for c in strs[0]]
        for s in strs[1:]:
            result = [r+c for r in result for c in s]
        return result


def main():
    digits = "23456789"
    s = Solution()
    print(s.letterCombinations(digits))


if __name__ == '__main__':
    main()
