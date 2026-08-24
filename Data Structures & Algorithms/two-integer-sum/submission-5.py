class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2: return [0,1]
        
        d = {}

        for i, n in enumerate(nums):
            if target-n in d:
                return [d[target-n],i]
            d[n] = i
        