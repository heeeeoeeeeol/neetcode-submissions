class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        d = {}

        for c in s1: d[c] = d.get(c,0) + 1

        for i in range(len(s1)):
            if s2[i] in s1:   
                d[s2[i]] -= 1
        
        flag = True
        for i in range(len(s1), len(s2)+1):
            print(d)

            for v in d.values():
                if v != 0: flag = False
            if flag: return True

            if i == len(s2): break

            if s2[i-len(s1)] in d:
                d[s2[i-len(s1)]] += 1
            if s2[i] in d:
                d[s2[i]] -= 1

            flag = True

        return False