class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missingNum = n = len(nums)

        for i in range(0,n):
            missingNum = missingNum ^ i #expected 
            missingNum = missingNum ^ nums[i] #actual 
        
        return missingNum
