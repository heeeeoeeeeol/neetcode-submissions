class Solution:
    def trap(self, height: List[int]) -> int:
        

        fill = [0] * len(height)

        h = 0
        for i, n in enumerate(height):
            if n >= h:
                h = n
                idx = i
            else:
                fill[i] = h-n

        h=0
        for i in range(len(height)-1,idx,-1):
            if height[i] >= h:
                h = height[i]
            fill[i] = h-height[i]

        ret = 0
        for f in fill: ret += f
        return ret
 
                
            


