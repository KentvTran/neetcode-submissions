class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, COLS - 1
        top, bottom = 0, ROWS - 1
        result = []

        while left <= right and top <=  bottom:
            #top row (left -> right)
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1
            #right col (top -> bottom )
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -=1

            #edge case
            if top > bottom or left > right:
                break
            #bottom row (right -> left)
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -=1
            #left col (bottom -> top)
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

        return result