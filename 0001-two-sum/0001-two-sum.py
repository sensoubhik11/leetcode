class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            if target-num in num_dict:
                return [i, num_dict[target-num]]
            num_dict[num] = i
        return [-1, -1]