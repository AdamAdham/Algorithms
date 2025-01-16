class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # To handle if k>n, we just get the extra part because if we shift n time it will remain the same
        if k==0:
            return nums

        nums[::] = nums[::-1] # Reverse array, why not nums = , because python is pass by assignment
        nums[:k] = nums[k-1::-1] # place in the first k elements the reversed order
        # why [k-1::-1]? because step is negative so start is at the LAST element, why k-1? because start index is inclusive and we want the first k elements
        nums[k:] = nums[:k-1:-1] # Starts from last element to k-1 because end index is exclusive