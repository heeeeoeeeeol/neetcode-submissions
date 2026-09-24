class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heap = []

        for pair in zip(heights, names):
            heapq.heappush_max(heap,pair)
        res = []
        while heap:
            res.append(heapq.heappop_max(heap)[1])
        return res