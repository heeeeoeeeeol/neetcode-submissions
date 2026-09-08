class Solution:
    def check(self, nums: List[int]) -> bool:
        numdec = 0
        prev = -1
        for i in range(len(nums)):
            if nums[i] < prev: 
                nums = nums[i:] + nums[:i]
                break
            prev = nums[i]

        return sorted(nums) == nums