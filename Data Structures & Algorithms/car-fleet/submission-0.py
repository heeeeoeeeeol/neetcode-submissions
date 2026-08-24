class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = reversed(sorted(list(zip(position,speed)), key=lambda x:x[0]))

        m = 0
        fcount = 0
        for c in cars:
            if (target-c[0])/c[1] > m:
                fcount += 1
                m = (target-c[0])/c[1] 

        return fcount