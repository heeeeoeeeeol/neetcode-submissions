class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            if c in d: d[c] += 1
            else: d[c] = 1
        for c in t: 
            if c not in d: return False
            if d[c] == 1: del d[c]
            else: d[c] -= 1
        return len(d) == 0
