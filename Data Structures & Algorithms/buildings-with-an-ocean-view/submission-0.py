class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        m = -1
        res = []
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > m:
                m = heights[i]
                res.append(i)

        return res[::-1]

        
        
