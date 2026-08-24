class MinStack:

    def __init__(self):
        self.st = []
        self.min = sys.maxsize

    def push(self, val: int) -> None:
        if not self.st: self.min = val
        self.st.append(val-self.min)
        self.min = min(self.min, val)

    def pop(self) -> None:
        if self.st[-1] < 0: self.min = self.min - self.st[-1]
        del self.st[-1]

    def top(self) -> int:
        return self.min if self.st[-1] < 0 else self.st[-1] + self.min 


    def getMin(self) -> int:
        return self.min
