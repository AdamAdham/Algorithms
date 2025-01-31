class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Description: Since the question is that each value is the max jumps index, so we can iterate through the array, with each iteration:
        we get the max jump value that can be achieved from previous jumps, when we finish the max we just update
        '''
        maxIndex = 0
        nextMaxIndex = 0
        i=0
        jumps = 0
        while i<len(nums) and i<=maxIndex:
            if maxIndex>=len(nums)-1:
                return jumps
            
            if i+nums[i]>nextMaxIndex:
                nextMaxIndex = i+nums[i]
            
            if i==maxIndex: # Reached the end of the current max index that can be achieved by the previous jump
                maxIndex = nextMaxIndex
                jumps+=1
            i+=1           
        return False