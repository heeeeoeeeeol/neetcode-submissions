class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d: self.d[key] = []
        self.d[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        lis = self.d[key]
        l, r = 0, len(lis)-1

        while l <= r:
            mid = (r+l)//2
            if lis[mid][1] > timestamp: r = mid-1
            elif lis[mid][1] < timestamp: l = mid+1
            else: return lis[mid][0]

        return lis[-1][0] if timestamp > lis[-1][1] else ""