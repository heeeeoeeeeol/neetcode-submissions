class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        for _ in range(k): heapq.heappush_max(gifts,int(heapq.heappop_max(gifts)**0.5))
        return sum(gifts)