class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        tdict = {}
        for c in t: tdict[c] = tdict.get(c,0) + 1
        sdict = {}
        have = 0
        need = len(tdict)
        l = 0

        shortl = -1
        shortr = len(s)

        for r, n in enumerate(s):
            if n in tdict:
                sdict[n] = sdict.get(n,0) + 1
                if sdict[n] == tdict[n]: have += 1
            while have == need:
                if (r-l < shortr-shortl):
                    shortl = l
                    shortr = r
                if s[l] in tdict:
                    sdict[s[l]] -= 1
                    if sdict[s[l]] < tdict[s[l]]:
                        have -= 1
                l += 1
                
        return "" if shortl == -1 else s[shortl:shortr+1]
        
