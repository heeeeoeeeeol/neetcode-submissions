class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        d = {}

        for c in s1: d[c] = d.get(c,0) + 1

        tmp = d.copy()

        i = 0
        while i < len(s2):
            if tmp.get(s2[i], 0) == 0:
                if s2[i] in d:
                    i-=1
                tmp = d.copy()
            else:
                if tmp[s2[i]] == 1:
                    del tmp[s2[i]]
                    if len(tmp) == 0: return True
                else:
                    tmp[s2[i]] -= 1
            i+=1

        return False
