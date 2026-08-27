class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        mask = 0
        
        def findPerm():    
            nonlocal res, perm, mask
            if len(perm) == len(nums):
                res.append(perm[:])  
                return
            for i, n in enumerate(nums):
                if not (mask & (1 << i)):
                    perm.append(n)
                    mask |= (1 << i)
                    findPerm()
                    mask &= ~(1 << i)
                    perm.pop()

        findPerm()
        return res
