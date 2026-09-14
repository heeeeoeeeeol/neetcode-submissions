class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wset, cache, mxl = set(wordDict), {len(s):True}, 0
        for w in wordDict: mxl = max(mxl,len(w))

        def dfs(i):
            if i in cache: return cache[i]
            for j in range(i, min(len(s),i+mxl)):
                if s[i:j+1] in wset:
                    if dfs(j+1): 
                        cache[i] = True
                        return True
            cache[i] = False
            return False

        return dfs(0)