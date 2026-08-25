class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}

        m = 0

        i=0
        while i < len(s):
            if s[i] not in d:
                d[s[i]] = i
            else:
                i = d[s[i]]
                d = {}
                
            if len(d) > m: m = len(d)
            i+=1

        return m
            



        