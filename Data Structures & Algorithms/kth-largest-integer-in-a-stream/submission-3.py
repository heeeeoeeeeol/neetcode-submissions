class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.l = sorted(nums) if k > len(nums) else sorted(nums)[-k:]
        self.k = k
        print(self.l)
        
    def add(self, val: int) -> int:
        self.l.append(val)
        self.l = sorted(self.l)
        if len(self.l) > self.k: self.l = self.l[-self.k:]
        return self.l[0]