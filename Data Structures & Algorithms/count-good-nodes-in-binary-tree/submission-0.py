# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countMax(self, root, m):
        if not root: return 0

        return 1+self.countMax(root.left,root.val)+self.countMax(root.right,root.val) if root.val >= m else self.countMax(root.left,m)+self.countMax(root.right,m)
            

    def goodNodes(self, root: TreeNode) -> int:
        return self.countMax(root, root.val)