class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1: return 1

        l = 0
        r = 1
        lidx = 0
        m = 0
        replace = 0

        while r < len(s):
            if s[r] != s[l]:
                if replace == k:
                    m = max(m, r-l)
                    l = lidx
                    r = l+1
                    replace = -1
                if replace == 0: 
                    lidx = r
                m = max(m, r-l+1)
                replace += 1
            m = max(m, r-l+1)
            r+=1

        return m