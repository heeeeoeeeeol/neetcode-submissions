class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c== ')': 
                if not st or st.pop() != '(': return False
                continue
            elif c== '}': 
                if not st or st.pop() != '{': return False
                continue
            elif c== ']': 
                if not st or st.pop() != '[': return False
                continue
            st.append(c)

        return len(st) == 0
            