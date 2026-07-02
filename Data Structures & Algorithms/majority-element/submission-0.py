class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        res = 0
        maxCount = 0

        for num in nums:
            freq[num] += 1
            if freq[num] > maxCount:
                res = num
                maxCount = freq[num]
        return res
            