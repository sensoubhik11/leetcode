class Solution:
    def reverse(self, nums, k):
        low, high = k, len(nums)-1
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1
            
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                k = i
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        break
                break
        self.reverse(nums, k)
        