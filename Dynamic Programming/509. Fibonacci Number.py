class Solution:
    fibArr = []
    def fib(self, n: int) -> int:
        if len(self.fibArr) <= n:
            self.fibArr = [0] * (n + 1)
        return self.helper(n)
    
    def helper(self, n: int) -> int:
        if n == 0:
            self.fibArr[n] = 0
        elif n == 1:
            self.fibArr[n] = 1
        elif self.fibArr[n] == 0:
            self.fibArr[n] = self.helper(n - 1) + self.helper(n - 2)
        
        return self.fibArr[n]
