class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9: 
            digits[-1]+=1
            return digits

        for i in range(len(digits)):
            digits[i] = str(digits[i])
        num = "".join(digits)
        num = str(int(num)+1)
        res = []
        for c in num:
            res.append(int(c))
        return res