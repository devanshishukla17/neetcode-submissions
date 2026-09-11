class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        cstack=[]
        cur=""
        k=0
        for c in s:
            if c.isdigit():
                k=k*10+int(c)
            elif c=="[":
                stack.append(cur)
                cstack.append(k)
                cur=""
                k=0
            elif c=="]":
                temp=cur
                cur=stack.pop()
                count=cstack.pop()
                cur+=temp*count
            else:
                cur+=c
        return cur