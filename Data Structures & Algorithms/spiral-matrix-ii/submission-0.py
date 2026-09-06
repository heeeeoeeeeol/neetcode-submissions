class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ma = [[0]*n for _ in range(n)]
        l, r, t, b, c = 0, n-1, 0, n-1, 1

        while l <= r:
            for i in range(l, r+1):
                ma[t][i] = c
                c += 1
            t += 1

            for i in range(t, b+1):
                ma[i][r] = c
                c += 1
            r -= 1
               
            for i in range(r, l-1, -1):
                ma[b][i] = c
                c += 1
            b -= 1
            
            for i in range(b, t-1, -1):
                ma[i][l] = c
                c += 1
            l += 1

        return ma