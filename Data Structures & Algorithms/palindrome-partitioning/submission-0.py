class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        pal = []

        def part(i, j):
            if i == len(s):
                if i == j: res.append(pal[:])
                return

            if s[j:i+1] == s[j:i+1][::-1]: 
                pal.append(s[j:i+1])
                part(i+1, i+1)
                pal.pop()
            part(i+1, j)

        part(0, 0)
        return res