import random

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        m = 0
        st = []

        for i, h in enumerate(heights):
            if not st or st[-1][1] < h:
                st.append([i,h])
                continue
            elif st[-1][1] == h: continue
            while st and st[-1][1] > h:
                i2, h2 = st.pop()
                m = max(m, h2*(i-i2))
            if i2 != i: st.append([i2,h])

        for s in st:
            m = max(m, s[1]*(len(heights)-s[0]))

        return m


            