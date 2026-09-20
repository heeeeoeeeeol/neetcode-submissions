class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            if n==1: return True
            seen.add(n)
            tmp = 0
            for c in str(n):
                tmp += int(c)**2
            n = tmp
        return False