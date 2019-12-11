"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？



例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28
"""


class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        result = 1

        def func(tm, tn, direct=None):
            nonlocal result
            if tm == m and tn == n:
                return

            if direct == "down":
                if tn < n:
                    if tm < m and tn < n:
                        result += 1
                    func(tm, tn+1, "right")
                if tm < m:
                    func(tm+1, tn, "down")
            elif direct == "right":
                if tn < n:
                    func(tm, tn+1, "right")
                if tm < m:
                    if tm < m and tn < n:
                        result += 1
                    func(tm+1, tn, "down")

        func(1, 1, "right")
        return result


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for i in range(m+1)]
        dp[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]


def main():
    m = 3
    n = 2
    obj = Solution2()
    print(obj.uniquePaths(m, n))


if __name__ == '__main__':
    main()
