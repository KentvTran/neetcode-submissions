class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]] #Base Case first row of Pascal's Triangle

        #numRows - 1: row 1 already made
        for i in range(numRows - 1):
            # add 0 pads/borders to previous rows 
            temp = [0] + res[-1] + [0]
            row = []

        #new row will be 1 element longer than previous row
            for j in range(len(res[-1]) + 1):
                #every element is sum of 2 element above it
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res
