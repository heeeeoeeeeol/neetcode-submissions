class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s)) + "x" + s
        return ret
    def decode(self, s: str) -> List[str]:
        print(s)
        ret = []
        word = ""
        l = ""

        i=0
        while len(s) - 1 >= i: 
            if s[i] != 'x': l += s[i]
            else: 
                word += s[i+1: i+1+int(l)]
                i += int(l) + 1
                ret.append(word)
                l = ""
                word = ""
                continue
            i+=1
        return ret