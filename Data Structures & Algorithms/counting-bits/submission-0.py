class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]

        for i in range(1, n + 1):
            output.append(output[i>>1] + (i % 2))
            #i>>1 is shifting binary to right or in other words diving by 2

        return output