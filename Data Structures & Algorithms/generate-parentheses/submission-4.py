class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        parens = []
        lc = 0
        rc = 0

        def dfs():
            nonlocal lc, rc
            if len(parens) == n*2:
                res.append("".join(parens))
                return

            if lc < n:
                parens.append("(")
                lc += 1
                dfs()
                parens.pop()
                lc -= 1
            if rc < lc:
                parens.append(")")
                rc += 1
                dfs()
                parens.pop()
                rc -= 1

        dfs()
        return res