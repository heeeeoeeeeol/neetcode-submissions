# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m = 0

        def nDepth(root):
            nonlocal m
            if not root:
                return 0
            l, r = nDepth(root.left), nDepth(root.right)
            m = max(m, l+r)
            return 1+max(l,r)

        nDepth(root)
        return m