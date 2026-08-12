class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        
        #dfs 
        def dfs(r,c):
            #base case; 
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 1:
                return 0
            grid[r][c] = "V"
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        #scanner loop
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    maxArea = max(maxArea, area)
        return maxArea
        