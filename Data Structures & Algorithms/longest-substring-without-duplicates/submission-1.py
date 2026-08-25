class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()

        l = 0
        m = 0
        for i, n in enumerate(s):
            if n not in d:
                d.add(n)
                l+=1
            else:
                l=1
                d.clear()
                d.add(n)
            if l > m: m = l

        return m
            



        
        