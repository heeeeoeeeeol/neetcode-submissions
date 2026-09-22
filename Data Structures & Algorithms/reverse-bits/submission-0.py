class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        mask = 1

        for i in range(31,-1,-1):
            res |= (1 if mask&n else 0)<<i
            mask <<= 1
        
        return res