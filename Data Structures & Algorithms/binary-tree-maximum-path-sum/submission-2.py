# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m = -sys.maxsize

        def maxSum(root):
            nonlocal m

            if not root: return 0

            lsum = maxSum(root.left)
            rsum = maxSum(root.right)
            m = max(m, root.val, root.val+lsum, root.val+rsum, root.val+lsum+rsum)

            if lsum < 0 and rsum < 0:
                return root.val
            elif rsum < 0:
                return root.val + lsum
            else:
                return root.val + rsum

        maxSum(root)
        return m