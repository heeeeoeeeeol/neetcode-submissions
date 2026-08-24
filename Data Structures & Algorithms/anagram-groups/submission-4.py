class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            if "".join(sorted(s)) in d: d["".join(sorted(s))].append(s)
            else: d["".join(sorted(s))] = [s]
        return list(d.values())

        
