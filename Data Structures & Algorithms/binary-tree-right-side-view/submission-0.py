# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque()
        q.append(root)

        res = []

        while q:
            lenq = len(q)
            for i in range(lenq):
                n = q.popleft()
                if i == lenq-1: res.append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)

        return res

