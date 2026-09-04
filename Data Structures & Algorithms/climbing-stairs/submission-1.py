class Solution:
    def climbStairs(self, n: int) -> int:
        s,prev = 1,0
        for _ in range(n):
            tmp = s
            s += prev
            prev = tmp
        return s