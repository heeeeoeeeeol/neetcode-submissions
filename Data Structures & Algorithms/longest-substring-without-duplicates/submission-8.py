class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        m = 0
        l=0

        for r in range(len(s)):
            if s[r] in d:
                l = max(d[s[r]] + 1,l)
            d[s[r]] = r
            m = max(m, r-l+1)
        return m
            



        