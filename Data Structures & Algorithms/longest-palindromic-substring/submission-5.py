class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = -1, 0  
        table = [[0]*len(s) for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(i+1):
                if s[j] == s[i] and (i-j <= 2 or table[j+1][i-1]):
                    table[j][i] = 1
                    if i-j+1 > resLen: 
                        resIdx = j 
                        resLen = i-j+1

        return s[resIdx:resIdx+resLen]