class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def findSub(i):
            nonlocal res, subset
            if i >= len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            findSub(i+1)
            subset.pop()
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            findSub(i+1)

        findSub(0)
        return res