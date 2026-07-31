# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def isValid(current, leftBound, rightBound):
            if not current:
                return True
            if not (current.val < rightBound and leftBound < current.val):
                return False
            return isValid(current.left, leftBound, current.val) and isValid(current.right, current.val, rightBound)
            

        return isValid(root, float("-inf"), float("inf"))