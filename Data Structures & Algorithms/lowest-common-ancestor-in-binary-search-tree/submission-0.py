# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findParent(self, root, child):
        par = None
        while root:
            if child.val > root.val:
                par = root
                root = root.right
            elif child.val < root.val:
                par = root
                root = root.left
            else:
                return par

    def isAncestor(self, n1, n2):
        while n1:
            if n2.val > n1.val:
                n1 = n1.right
            elif n2.val < n1.val:
                n1 = n1.left
            else:
                return True
        return False

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if self.isAncestor(p, q): return p
        elif self.isAncestor(q, p): return q

        return self.lowestCommonAncestor(root, self.findParent(root, p), self.findParent(root, q))