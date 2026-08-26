class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        #base case each number has a increasing sequence of at least 1
        dp = [1] * len(nums)

        #go up to last index
        for i in range(1,len(nums)):
            #check every number before i
            for j in range(0,i):
                #if previous number is smaller extend sequence
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
