import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        for c in tokens:
            if c in ops:
                op2 = st.pop()
                op1 = st.pop()
                st.append(ops[c](op1, op2) if c != "/" else int(ops[c](op1, op2)))

                print(ops[c](op1, op2))

            else:
                st.append(int(c))   

        return st[0]