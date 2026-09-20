class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==1: return 1
        if x==-1:
            return -1 if n%2 else 1
        if not n: return 1
        neg = False
        if n < 0:
            neg = True
            n*=-1

        res=x
        p = 1
        while 2*p <= n:
            res*=res
            p*=2

        n -= p
        while n:
            res*=x
            n-=1

        return res if not neg else 1/res
        