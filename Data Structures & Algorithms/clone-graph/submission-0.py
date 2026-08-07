"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #base case: if input graph is empty
        if not node:
            return None
        
        #maps orginal nodes to new cloned nodes
        oldToNew = {}
        
        #helper function to traverse graph and build clones
        def dfs(node):
            #if node is already cloned return clone
            if node in oldToNew:
                return oldToNew[node]
            
            #create new clone and save to map
            copy = Node(node.val)
            oldToNew[node] = copy

            #loop through all the neighbors in original node
            for neighbor in node.neighbors:
                #recursively clone each neighbor and add it to the copy's list
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)
        