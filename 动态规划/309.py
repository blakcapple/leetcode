# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 四种状态
        dp = [[0 for _ in range(4)] for _ in range(n)]
        # 0 持有股票状态；1 保持卖出股票状态；2 今天卖出股票；3 今天为冷冻期
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i], dp[i-1][3]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][3])
            dp[i][2] = max(dp[i-1][2], dp[i-1][0]+prices[i])
            dp[i][3] = dp[i-1][2]
        print(dp)
        result = max(dp[-1][1], dp[-1][2])
        result = max(result, dp[-1][3])
        return result
s = Solution()
prices = [1,2,3,0,2]
print(s.maxProfit(prices))