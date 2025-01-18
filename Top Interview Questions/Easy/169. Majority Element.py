class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # only count and curr element are needed
        count = 1
        current = nums[0]
        for i in range(1,len(nums)):
            if(current==nums[i]):
                count+=1
            else:
                count-=1
            if(count<0):
                current = nums[i]
                count = 1
        return current

