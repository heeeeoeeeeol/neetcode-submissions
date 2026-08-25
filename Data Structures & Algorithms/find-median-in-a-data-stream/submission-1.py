class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if not self.minheap or num > self.minheap[0]: heapq.heappush(self.minheap, num)
        else: heapq.heappush_max(self.maxheap, num)
    
        if len(self.minheap) - len(self.maxheap) == 2:
            heapq.heappush_max(self.maxheap, heapq.heappop(self.minheap))
        elif len(self.maxheap) - len(self.minheap) == 2:
            heapq.heappush(self.minheap, heapq.heappop_max(self.maxheap))

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap): return self.minheap[0]
        elif len(self.minheap) < len(self.maxheap): return self.maxheap[0]
        else: return (self.minheap[0] + self.maxheap[0])/2
        