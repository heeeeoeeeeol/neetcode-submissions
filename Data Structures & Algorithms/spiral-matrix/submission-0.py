class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        t,b,l,r = 0,m-1,0,n-1
        res = []

        while 1:
            for col in range(l,r+1): res.append(matrix[t][col])
            t+=1
            if l>r or t>b: break
            for row in range(t,b+1): res.append(matrix[row][r])
            r-=1
            if l>r or t>b: break
            for col in range(r,l-1,-1): res.append(matrix[b][col])
            b-=1
            if l>r or t>b: break
            for row in range(b,t-1,-1): res.append(matrix[row][l])
            l+=1
            if l>r or t>b: break


        return res
