class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = {}
        #loop through list
        for i, num in enumerate(nums):
            complementary = target - num
        #check if complementary is in result hash
            if complementary in result:
                return [result[complementary], i]
        #append number to result hash
            else:
                result[num] = i