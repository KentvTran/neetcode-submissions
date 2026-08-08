class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        ROWS, COLS = len(heights), len(heights[0])
        pacificFlow = set()
        atlanticFlow = set()

        #explorer
        def dfs(r,c,visitSet, prevHeight):
            if (r < 0 or c < 0 
            or r >= ROWS or c >= COLS
            or heights[r][c] < prevHeight or (r, c) in visitSet):
                return 
            visitSet.add((r, c))

            #explore all directions/recursion step
            dfs(r + 1, c, visitSet, heights[r][c])
            dfs(r - 1, c, visitSet, heights[r][c])
            dfs(r, c + 1, visitSet, heights[r][c])
            dfs(r, c - 1, visitSet, heights[r][c])

        for c in range(COLS):
            #top row (Pacific)
            dfs(0, c, pacificFlow, heights[0][c])
            #bottom row (Atlantic)
            dfs(ROWS-1, c, atlanticFlow, heights[ROWS-1][c])

        for r in range(ROWS):
            #left col (Pacific)
            dfs(r, 0, pacificFlow, heights[r][0])
            #right col (Atlantic)
            dfs(r, COLS-1, atlanticFlow, heights[r][COLS-1])
        return [[r, c] for r, c in (pacificFlow & atlanticFlow)]
