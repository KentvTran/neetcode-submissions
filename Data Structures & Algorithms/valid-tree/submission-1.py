class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        #build undirected adj list
        nodeMap = {i:[] for i in range(n)}
        for a,b in edges:
            nodeMap[a].append(b)
            nodeMap[b].append(a)
        #rack visited nodes
        visited = set()

        def dfs(node, prev):
            #base case cycle
            if node in visited:
                return False

            visited.add(node)

            #loop thru all connecting neighbors
            for neighbor in nodeMap[node]:
                #prevents looping backwards
                if neighbor == prev:
                    continue
                #if any neighbor detects cycle whole graph is invalid
                if not dfs(neighbor, node):
                    return False
            return True

        if not dfs(0,-1):
            return False

        #check if graph isn't split and number of node visited is equal to number of nodes
        return len(visited) == n

