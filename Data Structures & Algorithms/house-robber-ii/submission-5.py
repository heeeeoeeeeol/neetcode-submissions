class Solution:
    def rob(self, nums: List[int]) -> int:   
        cache = [0] * len(nums)
        def dfs(i, lis):
            if i >= len(lis): return 0
            if cache[i]: return cache[i]
            cache[i] = max(dfs(i+1, lis), lis[i]+dfs(i+2, lis))
            return cache[i]
        
        one = dfs(0,nums[1:])
        cache = [0] * len(nums)
        two = dfs(0,nums[:-1])
        return max(one,two,nums[0])