# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        q.append((root, -sys.maxsize))
        c = 0

        while q:
            n, m = q.popleft()
            if n.val >= m: c+=1
            if n.left: q.append((n.left, max(m, n.val)))
            if n.right: q.append((n.right, max(m, n.val)))

        return c

