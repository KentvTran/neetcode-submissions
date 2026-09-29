class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = counter = 0
        
        for num in nums:
            if num == 1:
                counter += 1
            elif num == 0:
                counter = 0
            result = max(result, counter)

        return result