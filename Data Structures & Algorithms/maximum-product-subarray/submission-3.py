class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]

        p, m = 1, -sys.maxsize
        for i in range(len(nums)):
            if not nums[i]:
                p = 1
                continue
            p *= nums[i]
            m = max(m, p)

        q = 1
        for i in range(len(nums)-1,-1,-1):
            if not nums[i]:
                q = 1
                continue
            q *= nums[i]
            m = max(m, q)

        return max(m,0)