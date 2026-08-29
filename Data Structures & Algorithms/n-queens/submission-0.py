class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queen = [["."]*n for _ in range(n)]
        cords = []
        res = []
        qc = 0

        def backtrack(r=0):
            nonlocal qc
            if r == n:
                if qc == n: res.append(["".join(q) for q in queen])
                return 

            for c in range(n):
                flag=True
                for cord in cords: 
                    if cord[1] == c or abs(cord[0]-r) == abs(cord[1]-c): 
                        flag = False
                        break
                if flag:
                    queen[r][c] = "Q"
                    qc += 1
                    cords.append([r,c])
                    backtrack(r+1)
                    queen[r][c] = "."
                    qc -= 1
                    cords.pop()

        backtrack()
        return res
