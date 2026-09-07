class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        for _ in range(k):
            m = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts,int(m**0.5))

        return sum(gifts)