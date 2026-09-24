class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        w1, w2 = 0, 0
        while w1 < len(word1) and w2 < len(word2):
            res += word1[w1] + word2[w2]
            w1, w2 = w1+1, w2+1

        if w1 < len(word1): res += word1[w1:]
        elif w2 < len(word2): res += word2[w2:]
        return res