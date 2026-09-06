class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = []
        for o in operations:
            if o == "+":
                l.append(l[-1]+l[-2])
            elif o == "C":
                l.pop()
            elif o == "D":
                l.append(l[-1]*2)
            else:
                l.append(int(o))

        return sum(l)