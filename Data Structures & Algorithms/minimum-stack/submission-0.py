class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        self.st.append([val, val if not self.st else min(val, self.st[-1][1])])

    def pop(self) -> None:
        del self.st[-1]

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]
