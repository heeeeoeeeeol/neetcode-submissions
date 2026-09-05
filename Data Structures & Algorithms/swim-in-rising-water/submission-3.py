class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = []
        heapq.heappush(heap,(grid[0][0],0,0))
        offset = [(1,0),(-1,0),(0,1),(0,-1)]
        vis = set()
        while heap:
            t,r,c = heapq.heappop(heap)
            if r==n-1 and c==n-1: return t
            if (r,c) in vis: continue
            vis.add((r,c))
            for dr, dc in offset:
                if 0<=r+dr<n and 0<=c+dc<n and (r+dr,c+dc) not in vis:
                    heapq.heappush(heap,(max(t,grid[r+dr][c+dc]),r+dr,c+dc))

        
