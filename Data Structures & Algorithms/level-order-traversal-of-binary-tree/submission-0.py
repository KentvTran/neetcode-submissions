# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = collections.deque() #fifo
        queue.append(root)

        while queue:
            levelLen = len(queue)
            currLevel = []

            for i in range(levelLen):
                node = queue.popleft()
                currLevel.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if currLevel:
                result.append(currLevel)
        return result