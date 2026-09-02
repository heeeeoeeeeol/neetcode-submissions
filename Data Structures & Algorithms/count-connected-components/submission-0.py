class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [0]*n
        self.comp = n

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
        self.comp -= 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = DSU(n)
        for e1, e2 in edges: uf.union(e1, e2)
        return uf.comp