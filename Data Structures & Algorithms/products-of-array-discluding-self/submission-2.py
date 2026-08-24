class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod = [1] * len(nums)
        rprod = [1] * len(nums)
        ret = [1] * len(nums)

        for i in range(len(nums)):    
            lprod[i] *= nums[i]
            if i > 0: lprod[i] *= lprod[i-1]
        
        for i in range(len(nums)-1, -1, -1):    
            rprod[i] *= nums[i]
            if i < len(nums)-1: rprod[i] *= rprod[i+1]
        
        for i in range(len(nums)):    
            if i == 0: ret[i] = rprod[i+1]
            elif i == len(nums)-1: ret[i] = lprod[i-1]
            else: ret[i] = lprod[i-1] * rprod[i+1]

        return ret


