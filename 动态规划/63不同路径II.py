# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

#机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

#现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

#网格中的障碍物和空位置分别用 1 和 0 来表示。

# from typing import List
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m = len(obstacleGrid[0]) # 列数
#         n = len(obstacleGrid) # 行数
#         dp = [[0 for _ in range(m)] for _ in range(n)]
#         dp[0][0] = 1
#         for i in range(n):
#             for j in range(m):
#                 if obstacleGrid[i][j] == 1:
#                     dp[i][j] = 0
#                 else:
#                     if i == 0 and j == 0:
#                         continue
#                     if i == 0:
#                         dp[i][j] = dp[i][j-1]
#                     elif j == 0:
#                         dp[i][j] = dp[i-1][j]
#                     else:
#                         dp[i][j] = dp[i-1][j] + dp[i][j-1]
#         print(dp)
#         return dp[-1][-1]

# o = [[0,0,0],[0,1,0],[0,0,0]]
# s.uniquePathsWithObstacles(o)

def fun(obstacleGrid):
    width = len(obstacleGrid[0])
    length = len(obstacleGrid)
    dp = [[0 for _ in range(width)] for _ in range(length)]
    for i in range(length):
        if obstacleGrid[i][0] == 1:
            break
        dp[i][0] = 1
    for j in range(width):
        if obstacleGrid[0][j] == 1:
            break
        dp[0][j] = 1
    for i in range(1,length):
        for j in range(1,width):
            if obstacleGrid[i][j]==1:
                continue
            if i-1 >=0 and obstacleGrid[i-1][j] == 0:
                dp[i][j] += dp[i-1][j]
            if j-1 >= 0 and obstacleGrid[i][j-1] == 0:
                dp[i][j] += dp[i][j-1]
    return dp
                
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(fun(obstacleGrid))