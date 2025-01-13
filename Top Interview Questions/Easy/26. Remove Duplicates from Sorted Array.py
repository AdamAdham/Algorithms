class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        place = 1
        compare = 1
        current = nums[0]
        while compare<len(nums):
            if(current!=nums[compare]):
                nums[place] = nums[compare]
                current = nums[compare]
                place+=1
                compare+=1
            else:
                # if current compare value is equal to the undesired value we just skip it, and maintain the index/count of the other values
                compare+=1
        k = place
        while place<len(nums):
            nums[place] = None
            place+=1

        return k