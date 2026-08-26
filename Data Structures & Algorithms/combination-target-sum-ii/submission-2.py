class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        s = 0
        candidates.sort()

        def findSub(i):
            nonlocal res, subset, s
            if s == target: 
                res.append(subset[:]) 
                return

            for j in range(i, len(candidates)):
                if s > target: return
                if j > i and candidates[j-1] == candidates[j]: continue

                subset.append(candidates[j])
                s+=candidates[j]
                findSub(j+1)
                subset.pop()
                s-=candidates[j]

        findSub(0)
        return res