class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        m = 0
        l=0

        for r in range(len(s)):
            if s[r] in d:
                l = d[s[r]] + 1
            d[s[r]] = r
            m = max(m, r-l+1)

        return m
            



        