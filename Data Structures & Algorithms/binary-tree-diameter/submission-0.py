# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
    
        #returns height
        def dfsHeight(curr):
            if not curr:
                return 0
            
            left = dfsHeight(curr.left)
            right = dfsHeight(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        
        dfsHeight(root)

        return self.res