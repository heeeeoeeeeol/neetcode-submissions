class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [0]*(len(s)+1)
        def dfs(i):
            if i >= len(s): return True
            if cache[i]: return True if cache[i] == 1 else False
            for w in wordDict:
                if len(s)-i >= len(w) and s[i:i+len(w)] == w:
                    if dfs(i+len(w)): 
                        cache[i] = 1
                        return True
            cache[i] = -1
            return False

        return dfs(0)