class Solution:
    def isValid(self, s: str) -> bool:
        open_p =['(','{','[']
        closed =[')','}',']']
        new_a=[]
        
        if len(s)%2==0:
            for i in range(len(s)):
                if s[i] in open_p:
                    new_a.append(s[i])
                if s[i] in closed:
                    if len(new_a)==0:
                        return False
                    if new_a[-1]=='(' and s[i]==')':
                        new_a.pop()
                    elif new_a[-1]=='[' and s[i]==']':
                        new_a.pop()
                    elif new_a[-1]=='{' and s[i]=='}':
                        new_a.pop()        
                    else:
                        return False
        else:
            return False 

        if(len(new_a)==0):
            return True
        else:
            return False 