class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        while i-1 >=0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums[:] = nums[::-1] #basically sort but since all are descending, using reverse
        else:
            j = len(nums)-1
            while j >= i and nums[j] <= nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
            nums[i:] = nums[i:][::-1]