# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        dq = deque()
        dq.append(root)

        ret = []

        while dq:
            ret.append([])
            for _ in range(len(dq)):
                n = dq.popleft()
                ret[-1].append(n.val)
                if n.left: dq.append(n.left)
                if n.right: dq.append(n.right)

        return ret
