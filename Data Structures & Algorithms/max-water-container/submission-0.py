class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        l = 0
        r = len(heights)-1
        while l < r:
            h = min(heights[l],heights[r])
            a = (r-l)*h
            if a > m: m=a

            if heights[l] > heights[r]: r-=1
            else: l+=1
            
        return m