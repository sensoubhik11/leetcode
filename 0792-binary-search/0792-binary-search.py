class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, low, high):
            if low <= high:
                mid = low + (high-low)//2
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    return binary_search(nums, low, mid-1)
                return binary_search(nums, mid+1, high)
            return -1
        return binary_search(nums,0,len(nums)-1)