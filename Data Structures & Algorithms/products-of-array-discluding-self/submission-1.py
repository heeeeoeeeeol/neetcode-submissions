class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(ret)):
                if i == j: continue
                ret[j] *= nums[i]

        return ret

