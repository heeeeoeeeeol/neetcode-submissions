class CountSquares:

    def __init__(self):
        self.d = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.d[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        for y in self.d[point[0]].keys():
            r = y-point[1]
            if not r: continue
            res += self.d[point[0]-r][point[1]]*self.d[point[0]-r][y]*self.d[point[0]][y] + self.d[point[0]+r][point[1]]*self.d[point[0]+r][y]*self.d[point[0]][y]
        return res