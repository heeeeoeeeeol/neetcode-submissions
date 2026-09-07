class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [0]*len(s)
        def dfs(i):
            if i == len(s): return 1
            if s[i] == "0": return 0
            if cache[i]: return cache[i]
            tmp = dfs(i+2) if i < len(s)-1 and s[i:i+2] <= "26" else 0 
            cache[i] = tmp + dfs(i+1)
            return cache[i]

        return dfs(0)