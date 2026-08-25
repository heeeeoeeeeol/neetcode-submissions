class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        m = 0
        d = set()

        while r < len(s):
            if s[r] not in d:
                d.add(s[r])
                r += 1
            else:
                m = max(m, r-l)
                d.remove(s[l])
                l += 1

        return m

                




        