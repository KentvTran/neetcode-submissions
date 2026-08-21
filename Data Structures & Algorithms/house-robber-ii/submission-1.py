class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        #base cases
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        #helper 
        def robHelper(houses):
            houseLen = len(houses)
            dp = [0] * houseLen
            #base cases
            dp[0] = houses[0]
            dp[1] = max(houses[0],houses[1]) 

            for i in range(2, houseLen):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            return dp[houseLen-1]

        
        #return max of two loops
        return max(robHelper(nums[0:n-1]), robHelper(nums[1:n]))
