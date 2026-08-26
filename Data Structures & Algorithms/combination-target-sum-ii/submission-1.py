class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        s = 0
        candidates.sort()

        def findSub(i):
            nonlocal res, subset, s
            if i >= len(candidates) or s > target:
                if s == target: res.append(subset[:])
                return

            subset.append(candidates[i])
            s+=candidates[i]
            findSub(i+1)
            subset.pop()
            s-=candidates[i]
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i+=1
            findSub(i+1)

        findSub(0)
        return res