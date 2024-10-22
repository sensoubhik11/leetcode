class Solution:
    def subsets_util(self, nums, temp, subset, i):
        if i == len(nums):
            subset.append(temp[:])
            return
        temp.append(nums[i])
        self.subsets_util(nums, temp, subset, i+1)
        temp.pop()
        self.subsets_util(nums, temp, subset, i+1)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp = []
        subset = []
        self.subsets_util(nums, temp, subset, 0)
        return subset