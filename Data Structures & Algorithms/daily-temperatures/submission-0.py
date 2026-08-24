class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ret = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            if not st or st[-1][0] >= n:
                st.append([n,i])
                continue
            while st and st[-1][0] < n:
                tmp = st.pop()
                ret[tmp[1]] = i - tmp[1]
            st.append([n,i])
            

        return ret