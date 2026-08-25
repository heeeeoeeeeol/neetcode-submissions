# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    m = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode], isFirst=True) -> int:
        if not root:
            return 0
        l, r = self.diameterOfBinaryTree(root.left, False), self.diameterOfBinaryTree(root.right, False)
        Solution.m = max(Solution.m, l+r)
        return Solution.m if isFirst else 1+max(l,r)

       