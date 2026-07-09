class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #get len of nums
        n = len(nums)

        #fill left and right array with 1s for n amount
        left = [1] * n
        right = [1] * n

        #make output array of len of nums
        output = [None] * n

        #build right array
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]

        #build left array
        for i in range(n - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        #build output
        for i in range(n):
            output[i] = left[i]*right[i]

        return output
