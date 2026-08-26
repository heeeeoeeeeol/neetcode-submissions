class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        ss = []
        s = 0
        def cSum(j=0):
            nonlocal res, s
            if s == target:
                res.append(ss[:])
                return

            for i in range(j, len(nums)):
                if s + nums[i] > target: return
                ss.append(nums[i])
                s += nums[i]
                cSum(i)                                      
                ss.pop()
                s -= nums[i]

        cSum()
        return res
