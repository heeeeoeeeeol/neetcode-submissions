class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0": return 0
        d = {}
        def dfs(s):   

            if not s or len(s) == 1 and s[0] != "0": return 1
            if s[0] == "0": return 0

            if s in d: return d[s]
            tmp = 0
            if s[:2] <= "26": tmp = dfs(s[2:]) 
            d[s] = tmp + dfs(s[1:]) 
            return d[s]

        return dfs(s)
