class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points:
            heapq.heappush(h, (point[0]**2+point[1]**2, point))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(h)[1])
        
        return res