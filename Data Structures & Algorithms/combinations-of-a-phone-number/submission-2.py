class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ch = [None,None,"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        def findComb(i):
            if i < 1: return [c for c in ch[int(digits[i])]]
            prev = findComb(i-1)
            temp, start, step =  prev * len(ch[int(digits[i])]), 0, len(prev)
            for c in ch[int(digits[i])]:
                for i in range(start, start+step): temp[i] += c
                start += step
            return temp

        if not len(digits): return []
        return findComb(len(digits)-1)
