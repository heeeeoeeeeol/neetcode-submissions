class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [0]*n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False
        if self.size[p1] >= self.size[p2]: p1, p2 = p2, p1
        self.parent[p1] = p2
        self.size[p2] += self.size[p1]
        return True 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = DSU(len(edges))
        for e in edges:
            if not uf.union(e[0]-1,e[1]-1): return e
