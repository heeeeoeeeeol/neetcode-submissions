class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for o in operations:
            match o:
                case "C": res.pop()
                case "+": res.append(res[-1] + res[-2])
                case "D": res.append(2*res[-1])
                case _: res.append(int(o))

        return sum(res)