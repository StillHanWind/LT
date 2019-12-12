"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""


class Solution1:
    def climbStairs(self, n: int) -> int:
        result = 0

        def func(tn):
            if tn == 0:
                nonlocal result
                result += 1
            if tn < 0:
                return
            func(tn-1)
            func(tn-2)

        func(n)

        return result


class Solution2:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        if n < 2:
            return dp[n]
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


def main():
    n = 3
    obj = Solution2()
    print(obj.climbStairs(n))


if __name__ == '__main__':
    main()
