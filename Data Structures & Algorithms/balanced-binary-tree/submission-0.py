# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True      
        
        def height(root):
            nonlocal flag
            if not root: return 0
            l = height(root.left)
            r = height(root.right)
            if abs(r-l)>1: flag = False
            return 1+max(l,r)

        height(root)
        return flag