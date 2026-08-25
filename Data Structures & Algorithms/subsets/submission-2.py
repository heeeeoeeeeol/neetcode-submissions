class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        subset = []
        def findsubs(i):
            if i >= len(nums):
                self.res.append(subset[:])
                return
            subset.append(nums[i])
            findsubs(i+1)
            subset.pop()
            findsubs(i+1)

        findsubs(0) 
        return self.res