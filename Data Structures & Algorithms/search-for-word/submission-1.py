class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board) #number of lists
        COLS = len(board[0]) #len of first list

        #tries to match word[i..] starting from cell(r,c)
        def dfs(r, c, i):
            #base case i == len(word) -> matched all chars
            if i == len(word):
                return True
            #fail cases; if out of bounds, current cells dont match word[i] or if cell is already used in our current path "#"
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            #mark cell the as used ("#")
            board[r][c] = '#'
            #try dfs in all directions down, up, right, left
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            #restore cell back/backtrack
            board[r][c] = word[i]
            return res

        #try every single cell in the grid as a starting point
        for r in range(ROWS):
            for c in range(COLS):
                #run dfs to look for first letter, if any starting point returns true -> word exists
                if dfs(r, c, 0):
                    return True
        return False
        