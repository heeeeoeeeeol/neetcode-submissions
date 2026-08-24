# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depthTree(root)

        m = 0

        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                m = max(m, node.val-1)
                if node.right and node.left: m = max(m, node.val + min(node.right.val, node.left.val) - 1)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return m




    def depthTree(self, root):
        if not root:
            return 0
        root.val = 1+max(self.depthTree(root.left), self.depthTree(root.right))
        return root.val