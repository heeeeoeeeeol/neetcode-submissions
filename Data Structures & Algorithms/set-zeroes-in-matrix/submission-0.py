class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        nr, nc = len(matrix), len(matrix[0])
        zrow, zcol = set(), set()

        for r in range(nr):
            for c in range(nc):
                if not matrix[r][c]: 
                    zrow.add(r)
                    zcol.add(c)

        for r in range(nr):
            for c in range(nc):
                if r in zrow or c in zcol:
                    matrix[r][c] = 0
