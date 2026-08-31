class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        #2D array m (rows) x n (columns) filled with 0s
        dp = [[0] * n for _ in range (m)]

        #Base Case 1: Fill first row with 1s (only one path)
        for c in range(n):
            dp[0][c] = 1

        #Base Case 2: Fill first column with 1s (only one path)
        for r in range(m):
            dp[r][0] = 1

        for c in range(1, n):
            for r in range(1, m):
            #to get to current, robot can come from either the left or from above current cell
                dp[r][c] = dp[r][c-1] + dp [r-1][c]
                
        return dp[m-1][n-1]