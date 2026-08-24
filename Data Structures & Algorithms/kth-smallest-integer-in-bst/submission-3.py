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
        kc, val = k, 0
        def findKth(node):
            nonlocal kc, val

            if not node: return
            findKth(node.left) 

            if kc == 0: return
            val = node.val
            kc -= 1

            findKth(node.right)

        findKth(root)
        return val