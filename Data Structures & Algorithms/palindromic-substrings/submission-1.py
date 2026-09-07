class Solution:
    def countSubstrings(self, s: str) -> int:
        table = [[0]*len(s) for _ in range(len(s))]
        res = 0

        for i in range(len(s)):
            for j in range(i+1):
                if s[i] == s[j] and (i-j <= 2 or table[j+1][i-1]):
                    table[j][i] = 1
                    res += 1
        return res