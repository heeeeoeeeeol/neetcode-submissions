class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        ss = []
        s = 0
        def cSum(i=0):
            nonlocal res, s
            if i >= len(nums) or s > target: return
            elif s == target:
                res.append(ss[:])
                return

            ss.append(nums[i])
            s += nums[i]
            cSum(i)                                      
            ss.pop()
            s -= nums[i]
            cSum(i+1)

        cSum()
        return res
