class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def findsubs(i):
            nonlocal nums 

            if i < 0: return [[]]

            res = findsubs(i-1)
            res2 = res[:]
            for r in res:
                r2 = r[:]
                r2.append(nums[i])
                res2.append(r2)
            return res2

        return findsubs(len(nums)-1)