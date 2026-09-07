class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        while k:
            m = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts,int(m**0.5))
            k -= 1

        return sum(gifts)