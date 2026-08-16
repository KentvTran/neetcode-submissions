class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        count = 0

        islandMap = {i: [] for i in range(n)}
        for a, b in edges:
            islandMap[a].append(b)
            islandMap[b].append(a)

        #to mark connected islands
        def dfs(island):
            visited.add(island)

            for neigh in islandMap[island]:
                if neigh not in visited: #only visit unvisited neighbors
                    dfs(neigh)
            
        #scanner for new clusters
        for ix in range(0, n):
            if ix not in visited: #if not explored already its a new cluster
                count += 1
                dfs(ix)
        return count
