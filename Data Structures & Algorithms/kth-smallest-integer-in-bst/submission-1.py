# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    kc = 1
    val = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return

        a = self.kthSmallest(root.left,k) 
        if a: return a

        Solution.val = root.val
        if Solution.kc == k: return Solution.val
        else: Solution.kc += 1

        a = self.kthSmallest(root.right,k)
        if a: return a
