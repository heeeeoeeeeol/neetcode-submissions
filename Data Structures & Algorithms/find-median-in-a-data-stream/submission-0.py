class MedianFinder:

    def __init__(self):
        self.h = []
        self.l = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.h, num)
        self.l += 1

    def findMedian(self) -> float:
        if self.l%2==1: return self.h[self.l//2]
        return (self.h[self.l//2] + self.h[self.l//2-1])/2