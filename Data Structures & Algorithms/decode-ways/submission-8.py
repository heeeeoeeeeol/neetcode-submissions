class Solution:
    def numDecodings(self, s: str) -> int:
        one, two = 1, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0": tmp = 0
            elif i < len(s)-1 and s[i:i+2] <= "26": tmp = one + two
            else: tmp = one
            two = one
            one = tmp

        return one