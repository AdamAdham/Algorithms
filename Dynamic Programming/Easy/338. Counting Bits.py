class Solution:
    def countBits(self, n: int) -> List[int]:
        if n<0:
            return None
        array = [0]*(n+1)
        if(n<1):
            return array
        array[1] = 1
        dec = 1
        for i in range(2, n+1):
            array[i] = 1 + array[i-2**int(log2(i))]
        return array
