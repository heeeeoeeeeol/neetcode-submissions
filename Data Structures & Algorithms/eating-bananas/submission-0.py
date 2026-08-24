class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        high = max(piles)
        low = 1
        
        if h == len(piles): return high
        elif h >= sum(piles): return low

        while high >= low:
            k = (high + low) // 2

            count = 0
            for p in piles:
                count += -(-p // k)

            if count <= h: 
                high = k-1
                res = k
            elif count > h: low = k+1
            
        return res


            

   
