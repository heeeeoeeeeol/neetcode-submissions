class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<len(s):
                if s[l] != s[r]:
                    break
                if r-l+1 > len(res): res = s[l:r+1]
                l-=1
                r+=1
                
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                l,r = i-1,i
                while l>=0 and r<len(s):
                    if s[l] != s[r]:
                        break
                    if r-l+1 > len(res): res = s[l:r+1]  
                    l-=1
                    r+=1

        return res