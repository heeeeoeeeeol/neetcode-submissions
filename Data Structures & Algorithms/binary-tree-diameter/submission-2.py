# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, m = self.depthTree(root)
        m = max(root.val-1, m)
        if root.right and root.left: m = max(m, root.val + min(root.right.val, root.left.val) - 1)

        return m
        


    def depthTree(self, root, m=0):
        if not root:
            return 0, 0
        r1, m = self.depthTree(root.left,m)
        r2, m = self.depthTree(root.right,m)
        root.val = 1+max(r1, r2)
        m = max(m, root.val-1)
        if root.right and root.left: m = max(m, root.val + min(root.right.val, root.left.val) - 1)
        return root.val, m