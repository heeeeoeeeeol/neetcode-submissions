class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = [[]]
        for i in range(len(nums)):
            tmp = []
            for p in perm: tmp += [p[:j] + [nums[i]] + p[j:] for j in range(i+1)]
            perm = tmp

        return perm
