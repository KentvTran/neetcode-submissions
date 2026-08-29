class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #initialize array
        dp = [float("inf")] * (amount+1)

        dp[0] = 0
        #loop through 0 -> amount 
        for i in range(1, amount+1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i-c]+1)
        
        if dp[amount] == float("inf"): 
            return -1 
        else:
            return dp[amount]