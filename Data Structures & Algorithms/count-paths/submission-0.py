class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #2D Matrix mxn: dp[r][c] = total # of unique paths to get to (r,c)
        #top row and first column only has one path
        dp = [[1] * n for _ in range(m)]
        
        #top row and first column only has one path
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[m-1][n-1]
