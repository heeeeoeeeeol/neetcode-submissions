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
        q = deque()
        q.append(node)
        ht = {}
        ht[node] = Node(node.val)

        while q:
            n = q.pop()
            
            for adj in n.neighbors:
                if adj not in ht:
                    q.append(adj)
                    ht[adj] = Node(adj.val)
                ht[n].neighbors.append(ht[adj])

        return ht[node]


