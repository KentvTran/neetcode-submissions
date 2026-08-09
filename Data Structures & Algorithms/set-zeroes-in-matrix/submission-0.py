class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        firstColZero = False

        #scan for 0 and set flags
        for r in range(0, ROWS):
            if matrix[r][0] == 0:
                firstColZero = True
            #check rest of the row
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[r][0], matrix[0][c] = 0,0
        
        #update inner matrix based on flags:
        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        #cleanup 
        #did first row have a zero
        if matrix[0][0] == 0:
            for c in range(0,COLS):
                matrix[0][c] = 0
        #did first col have zero:
        if firstColZero:
            for r in range(0, ROWS):
                matrix[r][0] = 0
        
        