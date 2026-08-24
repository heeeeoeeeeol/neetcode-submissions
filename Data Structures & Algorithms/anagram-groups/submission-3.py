class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0: return []
        elif len(strs) == 1: return [strs]

        ret = []

        d = {}
        for ch in strs[0]:
            if ch in d: d[ch] += 1
            else: d.setdefault(ch, 1)
        
        sub = [strs[0]]
        temp = []

        for i in range(1, len(strs)):
            d2 = d.copy()
            if len(strs[i]) != len(strs[0]): 
                temp.append(strs[i])
                continue
            for ch in strs[i]:
                if ch not in d2: 
                    temp.append(strs[i])
                    break
                else:
                    if d2[ch] > 1: d2[ch] -= 1
                    else: del d2[ch]
            if len(d2) == 0: sub.append(strs[i])


        ret.append(sub)
        for s in self.groupAnagrams(temp): ret.append(s)
        return ret
        
