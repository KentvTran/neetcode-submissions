class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0


        while r < n:

            nums[l] = nums[r]
            #skip duplicates
            while r < n and nums[r] == nums[l]:
                r += 1
            #after skipping duplicate move left pointer and copy current element at r to new l position
            l += 1
        return l