class Solution:
    def mySqrt(self, x: int) -> int:
        avg= round(x/2)+1
        for i in range(0,x+1):    
            if(i*i>x):
                return i-1
            elif(i*i==x):
                return i 
