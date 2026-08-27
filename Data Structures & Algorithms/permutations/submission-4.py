class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        used = [False]*len(nums)
        def findPerm():    
            nonlocal res, perm, used
            if len(perm) == len(nums):
                res.append(perm[:])  
                return
            for i, n in enumerate(nums):
                if not used[i]:
                    perm.append(n)
                    used[i] = True
                    findPerm()
                    used[i] = False
                    perm.pop()

        findPerm()
        return res
