class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) #nxn matrix

        #only loop through top right triangle of matrix
        #transpose 
        for r in range(n):
            for c in range(r,n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        #reverse each row
        for r in range(n):
            matrix[r].reverse()