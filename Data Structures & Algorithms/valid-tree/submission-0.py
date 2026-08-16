class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        #build undirected adj list
        nodeMap = {i:[] for i in range(n)}
        for a,b in edges:
            nodeMap[a].append(b)
            nodeMap[b].append(a)
        visited = set()

        def dfs(node, prev):
            #base case cycle
            if node in visited:
                return False

            visited.add(node)

            for neighbor in nodeMap[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        if not dfs(0,-1):
            return False

        return len(visited) == n

