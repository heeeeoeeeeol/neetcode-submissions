class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0 
        ht = {}
        for n in nums:
            res += ht.get(n, 0)
            ht[n] = ht.get(n, 0) + 1

        return res