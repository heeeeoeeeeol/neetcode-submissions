class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def makePerm(i):
            if i < 0: return [[]]
            perm = makePerm(i-1)
            tmp = []
            for p in perm: tmp += [p[:j] + [nums[i]] + p[j:] for j in range(i+1)]
            return tmp
            
        return makePerm(len(nums)-1)
