# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidNode(node, mi, ma):
            if not node: return True

            if node.val > mi and node.val < ma:
                return isValidNode(node.left, mi, node.val) and isValidNode(node.right, node.val, ma)
            return False

        return isValidNode(root, -sys.maxsize, sys.maxsize)
