class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def makePerm(i):
            if i < 0: return [[]]
            perm = makePerm(i-1)[:]
            tmp = []
            for p in perm:
                for j in range(i+1):
                    tmp.append(p[:j] + [nums[i]] + p[j:])
            return tmp

        return makePerm(len(nums)-1)
