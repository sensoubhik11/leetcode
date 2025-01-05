class Solution:
    def merge(self, nums, low, mid, high):
        # counting
        cnt = 0
        left = nums[low:mid+1]
        right = nums[mid+1:high+1]
        j = 0
        for i in range(len(left)):
            while j < len(right) and left[i] > 2*right[j]:
                j += 1
            cnt += j

        # merging
        l, r, k = 0, 0, low
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                nums[k] = left[l]
                l += 1
            else:
                nums[k] = right[r]
                r += 1
            k += 1
        while l < len(left):
            nums[k] = left[l]
            l += 1
            k += 1
        while r < len(right):
            nums[k] = right[r]
            r += 1
            k += 1
        return cnt
        
    def modified_merge_sort(self, nums, low, high):
        if low < high:
            mid = low + (high-low)//2
            count = self.modified_merge_sort(nums, low, mid)
            count += self.modified_merge_sort(nums, mid+1, high)
            count += self.merge(nums, low, mid, high)
            return count
        return 0
    def reversePairs(self, nums: List[int]) -> int:
        return self.modified_merge_sort(nums, 0, len(nums)-1)