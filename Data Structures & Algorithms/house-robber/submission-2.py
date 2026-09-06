class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        maxpay = [0]*len(nums)
        maxpay[0] = nums[0]
        maxpay[1] = max(nums[0],nums[1])

        for i in range(2, len(nums)):
            maxpay[i] = max(maxpay[i-1], nums[i]+maxpay[i-2])

        return maxpay[-1]