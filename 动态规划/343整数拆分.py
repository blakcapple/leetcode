#给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。

#返回 你可以获得的最大乘积 。

# class Solution:
#     def integerBreak(self, n: int) -> int:
#         dp = [0] * (n+1) 
#         dp[1] = 1
#         dp[2] = 1
#         for i in range(3,n+1):
#             for j in range(1, n):
#                 idx = i - j
#                 dp[i] = max(dp[i], j*dp[idx], j*idx)
#         print(dp)
#         return dp[-1]
    
# s = Solution()
# n = 5
# s.integerBreak(n)


def fun(n):
    dp = [0 for i in range(n+1)]
    dp[1] = 1 
    dp[2] = 1
    if n ==  1 or n == 2:
        return 1
    for i in range(1, n+1):
        for j in range(1, n):
            dp[i] = max(dp[j] * (i-j), dp[i], i-1, j*(i-j)) 
    return dp[-1]

print(fun(8))