class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c = 0,1,1
        
        for i in range(n):
            a,b,c = b,c,a+b+c
        if(n<0):
            return -1
        return a
        
