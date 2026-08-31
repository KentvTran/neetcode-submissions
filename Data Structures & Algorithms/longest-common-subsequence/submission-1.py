class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS = len(text1)+1
        COLS = len(text2)+1
        dp = [[0] * COLS for _ in range(ROWS)]

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if text1[r-1] == text2[c-1]:
                    dp[r][c] = 1 + dp[r-1][c-1]
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        return dp[ROWS-1][COLS-1]