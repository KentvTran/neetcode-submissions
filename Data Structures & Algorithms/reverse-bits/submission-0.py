class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range (32):
            #extract bit using (n>>1) & 1
            bit = (n>>i) & 1
        
            # if 1 set bit in res at position (31-i) using res |= (1 << (31-i))
            if bit:
                res |= (1 << (31-i))
        
        return res