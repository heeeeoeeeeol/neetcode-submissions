class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}

        l = 0
        max_freq = 0
        m = 0

        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1
            max_freq = max(max_freq, d[s[r]])
            if r-l+1-max_freq > k:
                d[s[l]] -= 1
                l+=1
            m = max(m, r-l+1)

        return m
            


