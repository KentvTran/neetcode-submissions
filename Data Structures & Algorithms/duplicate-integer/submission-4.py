class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkHash = set()

        for number in nums:
            if number in checkHash:
                return True
            checkHash.add(number)
        return False
         