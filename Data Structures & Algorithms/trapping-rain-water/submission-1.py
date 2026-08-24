class Solution:
    def trap(self, height: List[int]) -> int:
        

        temp = 0

        h = 0
        for i, n in enumerate(height):
            if n >= h:
                h = n
                idx = i
                left = temp
            else:
                temp += h-n

        h=0
        for i in range(len(height)-1,idx,-1):
            if height[i] >= h:
                h = height[i]
            left += h-height[i]

        return left
 
                
            


