class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = {i:[] for i in range(n)}
        for a, b in edges: 
            d[a].append(b)
            d[b].append(a)

        vis = set()
        def dfs(i=0, par=-1):
            if i in vis: return False
            vis.add(i)
            for j in d[i]: 
                if j == par: continue
                if not dfs(j, i): return False
            return True
            
        
        return dfs() and len(vis) == n
