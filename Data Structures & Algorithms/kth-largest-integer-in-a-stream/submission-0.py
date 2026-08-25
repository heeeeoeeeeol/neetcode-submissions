class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.l = sorted(nums)[-k:]
        
    def add(self, val: int) -> int:
        if val > self.l[0]:
            self.l.append(val)
            self.l.pop(0)
            self.l = sorted(self.l)
            return self.l[0]
        elif val == self.l[0]:
            return val
