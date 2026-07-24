class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n: #while n isnt 0
            count += n % 2  #count gets added 0 or 1
            n = n >> 1      #move bit by 1 to the right
        
        return count