class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # ex: coins = [1,2], amount = 3

        #initialize array with inf
        dp = [float("inf")]* (amount + 1)

        #base case
        #dp is [0, inf, inf, inf]
        dp[0] = 0

        #loop through from 1 to target (1,2,3)
        for i in range(1, amount + 1):
            for c in coins:
            #check if current coin is less than current amount
                if c <= i:
            #min of current best or previous amount + 1 coin used
                    dp[i] = min(dp[i], dp[i - c] + 1)
        
        return dp[amount] if dp[amount] != float("inf") else -1
