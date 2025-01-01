class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = -1
        mid = 0
        high = len(nums)
        while mid < high:
            if nums[mid] == 0:
                low += 1
                nums[mid], nums[low] = nums[low], nums[mid]
                mid += 1
            elif nums[mid] == 2:
                high -= 1
                nums[high], nums[mid] = nums[mid], nums[high]
            else:
                mid += 1