class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums = sorted(nums)

        for i, n in enumerate(nums):
            for j in range(i+1, len(nums)):
                if -n-nums[j] in nums[j+1:]:
                    if [n,nums[j],-n-nums[j]] not in ret:
                        ret.append([n,nums[j],-n-nums[j]])

        return ret