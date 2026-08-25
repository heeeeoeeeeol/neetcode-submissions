class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2: return [0,1]
        d = {}
        for i in range(len(nums)): d[target - nums[i]] = i
        for i in range(len(nums)): 
            if nums[i] in nums: return [i,d[nums[i]]]

        