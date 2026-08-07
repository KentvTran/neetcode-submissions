class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islandCount = 0

        #dfs helper/explorer function
        def dfs(r, c):
            #base case if out of bounds or not 1
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1":
                return
            #mark current cell as visited
            grid[r][c] = "V"
            #explore all 4 directions/recursion 
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        #scanner
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    islandCount += 1
                    dfs(r,c)

        return islandCount