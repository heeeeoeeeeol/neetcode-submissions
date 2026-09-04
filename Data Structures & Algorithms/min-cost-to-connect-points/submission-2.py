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
        if self.size[p1] >= self.size[p2]: p2, p1 = p1, p2
        self.parent[p1] = p2
        self.size[p2] += self.size[p1]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int: 
        uf = DSU(len(points))
        l = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j: continue
                l.append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),i,j))
     
        l.sort(key=lambda x:x[0])
        edges, res = 0, 0
        for p in l:
            if uf.union(p[1],p[2]): 
                res += p[0]
                edges += 1
            if edges == len(points)-1: return res

        return 0

                
