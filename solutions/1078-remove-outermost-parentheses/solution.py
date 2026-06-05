class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        f=[]
        count=0
        for i in s:
            stack.append(i)
            if i=='(':
                count+=1
            elif i==')':
                count-=1
            if count==0:
                f+=stack[1:-1]
                stack=[]
        return "".join(f)
        
