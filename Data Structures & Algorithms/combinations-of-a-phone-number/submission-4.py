class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ch = [None,None,"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = [""]

        for i in digits:
            tmp = []
            for l in res:
                for c in ch[int(i)]: 
                    tmp.append(l+c)
            res = tmp
        return res if digits else []
