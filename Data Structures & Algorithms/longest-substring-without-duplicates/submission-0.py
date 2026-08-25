class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}

        l = 0
        m = 0
        for i, n in enumerate(s):
            d[n] = d.get(n, 0) + 1
            l+=1
            if d[n] > 1:
                l=0
                d = {}
                continue
            elif l > m: m = l

        return m
            



        
        