"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
"""

from typing import List


class Solution1:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length = len("".join(words))
        if len(s) < length or not s or not words:
            return []

        def get_words(string):
            if len(string) == 0:
                return [string]
            results = []
            for i in range(len(string)):
                for item in get_words(string[:i] + string[i + 1:]):
                    results.append([string[i]] + item)
            return results

        words = ["".join(t) for t in get_words(words)]
        index = 0
        result = list()
        while index < len(s):
            end = index+length
            if s[index:end] in words:
                result.append(index)
            index += 1

        return result


class Solution2:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length = len("".join(words))
        if len(s) < length or not s or not words:
            return []
        length_one = len(words[0])

        d = dict()
        for w in words:
            if w not in d:
                d[w] = 1
            else:
                d[w] += 1
        result = list()
        for index in range(len(s)-length+1):
            ts = s[index:index+length]
            td = d.copy()
            for i in range(len(words)):
                tts = ts[i*length_one:(i+1)*length_one]
                print(tts)
                if tts in td and td[tts] != 0:
                    td[tts] -= 1
                else:
                    break
            else:
                result.append(index)
        return result


def main():
    string = "wordgoodbestword"
    words = ["word", "good", "best", "word"]
    s = Solution2()
    print(s.findSubstring(string, words))


if __name__ == '__main__':
    main()
