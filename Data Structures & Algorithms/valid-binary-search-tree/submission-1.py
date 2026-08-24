# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append((root, -sys.maxsize, sys.maxsize))

        while q:
            node, mi, ma = q.popleft()
            if not ma > node.val > mi: return False
            if node.left: q.append((node.left, mi, node.val))
            if node.right: q.append((node.right, node.val, ma))

        return True