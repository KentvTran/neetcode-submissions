class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #pointer to zero
        j = -1

        #find zero
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break
        #if no zero found return
        if j == -1:
            return

        #start from next index of first zero
        for i in range(j + 1, len(nums)):
            #if curr is non zero
            if nums[i] != 0:
                #swap with first zero (j)
                nums[i], nums[j] = nums[j], nums[i]
                #move j to next zero
                j += 1