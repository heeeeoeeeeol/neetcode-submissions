class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)

        res = 1
        for i in range(len(nums)-2,-1,-1):
            tmp = 1
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]: tmp = max(tmp, dp[j]+1)
            res = max(res, tmp)
            dp[i] = tmp

        return res