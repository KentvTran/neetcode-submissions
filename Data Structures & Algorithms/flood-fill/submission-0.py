class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]

        if originalColor == color:
            return image

        #dfs to explore original color
        def dfs(r,c):
            #base case: boundary & not og color
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != originalColor:
                return 
            image[r][c] = color

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        dfs(sr,sc)
        return image