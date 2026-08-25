class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        m = 0
        l=0

        for r in range(len(s)):
            if s[r] in d:
                m = max(m, r-l)
                l = d[s[r]] + 1
            d[s[r]] = r

        return max(m, r-l)
            



        