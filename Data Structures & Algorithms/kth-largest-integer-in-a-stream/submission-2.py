class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.l = sorted(nums)[-k:]
        print(self.l)
        
    def add(self, val: int) -> int:
        if val > self.l[0]:
            self.l.append(val)
            self.l.pop(0)
            self.l = sorted(self.l)
            return self.l[0]
        else:
            return self.l[0]
