"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        ht = {}

        def dfs(n):
            if n.val in ht: return ht[n.val]

            ht[n.val] = Node(n.val)
            for adj in n.neighbors:
                ht[n.val].neighbors.append(dfs(adj))

            return ht[n.val]
                
        return dfs(node)
