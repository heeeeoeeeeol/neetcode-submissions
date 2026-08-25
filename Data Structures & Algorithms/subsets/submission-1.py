class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def findsubs(i):
            nonlocal nums 
            if i < 0: return [[]]
            res = findsubs(i-1)
            res += [r + [nums[i]] for r in res]
            return res
        return findsubs(len(nums)-1)