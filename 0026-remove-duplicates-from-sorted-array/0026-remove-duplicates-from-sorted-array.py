class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        cur_idx = 1
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[cur_idx] = nums[i]
                cur_idx += 1
                prev = nums[i]
        return cur_idx