"""
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        string = '1'
        i = 1

        def count(i, s):
            if i == n:
                return s
            t = s[0]
            result = ""
            cou = 0
            for c in s:
                if c == t:
                    cou += 1
                else:
                    result += (str(cou) + t)
                    t = c
                    cou = 1
            result += (str(cou) + t)
            i += 1
            return count(i, result)

        return count(i, string)


def main():
    n = 30
    s = Solution()
    print(s.countAndSay(n))


if __name__ == '__main__':
    main()
