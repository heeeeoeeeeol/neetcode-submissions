class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = reversed(sorted(list(zip(position,speed)), key=lambda x:x[0]))

        st = []
        for c in cars:
            if not st or (target-c[0])/c[1] > st[-1]:
                st.append((target-c[0])/c[1])
        return len(st)