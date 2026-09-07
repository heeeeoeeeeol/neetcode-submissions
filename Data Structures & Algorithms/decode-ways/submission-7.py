class Solution:
    def numDecodings(self, s: str) -> int:
        d = [0]*(len(s)+1)
        d[len(s)] = 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0": continue
            if i < len(s)-1 and s[i:i+2] <= "26": d[i] = d[i+2] + d[i+1]
            else: d[i] = d[i+1]

        return d[0]