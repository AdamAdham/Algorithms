class Solution:
    def jump(self, nums: List[int]) -> int:
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
        return -1