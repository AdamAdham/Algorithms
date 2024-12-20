class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        returnValue = []
        if(numRows==1):
            returnValue = [[1]]
        if(numRows>1):
            returnValue = [[1],[1,1]]
        for i in range(2,numRows):
            rowList = [1]*(i+1)
            for j in range(1,len(rowList)-1):
                # Because both first and last element are always 1
                rowList[j] = returnValue[i-1][j-1] + returnValue[i-1][j]
            returnValue+=[rowList]
        return returnValue
