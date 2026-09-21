class CountSquares:

    def __init__(self):
        self.d = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.d[point[0],point[1]] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        for key in self.d.keys():
            if abs(key[0]-point[0]) == abs(key[1]-point[1]):
                if key != (point[0],point[1]) and (key[0],point[1]) in self.d and (point[0],key[1]) in self.d:
                    res += self.d[key[0],point[1]]*self.d[point[0],key[1]]*self.d[key[0],key[1]]
        return res
