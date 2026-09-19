class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for t in tokens:
            if t=="+":
                st.append(st.pop()+st.pop())
            elif t=="-":
                a,b=st.pop(),st.pop()
                st.append(b-a)
            elif t=="*":
                st.append(st.pop()*st.pop())
            elif t=="/":
                a,b=st.pop(),st.pop()
                st.append(int(float(b)/a))
            else:
                st.append(int(t))
        return st[0]