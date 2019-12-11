"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t = {tuple(sorted([c for c in s])) if s else s: list() for s in strs}
        for s in strs:
            # if not s:
            #     t[s].append(s)
            #     continue
            # if s not in t[tuple(sorted([c for c in s]))]:
            t[tuple(sorted([c for c in s])) if s else s].append(s)
        return [i for i in t.values()]


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # strs = ["", ""]
    obj = Solution()
    print(obj.groupAnagrams(strs))


if __name__ == '__main__':
    main()
