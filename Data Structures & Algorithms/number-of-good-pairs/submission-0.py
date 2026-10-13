class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        visited = {} #number: count
        pairs = 0

        #traverse nums
        for num in nums:
            pairs += visited.get(num, 0)
            visited[num] = visited.get(num, 0) + 1

        return pairs
            
            
        