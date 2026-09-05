class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int: 
        heap = []
        heapq.heappush(heap, (0,points[0][0], points[0][1]))
        vis, res = set(), 0

        while len(vis) < len(points):
            d, x, y = heapq.heappop(heap)      
            if (x, y) in vis: continue   
            res += d   
            vis.add((x,y))
            for x2, y2 in points:
                if (x2, y2) in vis: continue
                heapq.heappush(heap, (abs(x-x2)+abs(y-y2),x2,y2))

        return res