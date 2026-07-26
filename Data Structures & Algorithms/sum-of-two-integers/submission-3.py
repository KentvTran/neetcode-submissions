class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        for i in range(32):
            bitA = (a >> i) & 1
            bitB = (b >>i) & 1

            currentBit = bitA ^ bitB ^ carry
            carry = (bitA & bitB) | (bitA & carry) | (bitB & carry)
    
            if currentBit:
                 res |= (1 << i)

            if res > 0x7FFFFFFF:
                res = ~(res ^ 0xFFFFFFFF)
        return res
        