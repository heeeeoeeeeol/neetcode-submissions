class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2: return [0,1]
        
        d = {}

        for i in range(len(nums)):
            if d.get(target-nums[i]) == None: d[nums[i]] = i
            else: return [d[target-nums[i]], i]
                
        