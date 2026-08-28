class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ch = [None,None,"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = []

        def findComb(i=0, comb=""):
            if i == len(digits): 
                res.append(comb)
                return
            for c in ch[int(digits[i])]: findComb(i+1, comb+c)

        if digits: findComb()
        return res
