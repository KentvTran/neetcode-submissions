class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #furthest index so far
        maxReach = 0

        for ix, val in enumerate(nums):
            #if current position is further than maxReach -> we got stuck on a zero
            if ix > maxReach:
                return False
            #update furthest reach
            maxReach = max(maxReach, ix + val)
        return True