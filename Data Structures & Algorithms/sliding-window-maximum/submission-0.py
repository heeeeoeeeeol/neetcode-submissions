import heapq 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): return max(nums)
        
        ret = [0]*(len(nums)-k+1)

        ltable = [0]*len(nums)
        rtable = [0]*len(nums)

        for i in range(len(nums)):
            if i%k==0:
                fill = nums[i]
            elif nums[i] > fill:
                fill = nums[i]
            ltable[i] = fill

        fill = nums[len(nums)-1]
        for i in range(len(nums)-1, -1, -1):
            if (i+1)%k==0:
                fill = nums[i]
            elif nums[i] > fill:
                fill = nums[i]
            rtable[i] = fill

        print(ltable)
        print(rtable)

        for r in range(k-1, len(nums)):
            ret[r-k+1] = max(ltable[r],rtable[r-k+1])

        return ret
            


         
