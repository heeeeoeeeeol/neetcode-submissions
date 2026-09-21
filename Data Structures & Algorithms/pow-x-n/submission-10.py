class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        p = abs(n)
        res = 1
        while p:
            if p&1: res*=x
            x*=x
            p>>=1
        return res if n>0 else 1/res