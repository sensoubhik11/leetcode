class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def subset_util(idx, ds):
            res.append(ds[:])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                ds.append(nums[i])
                subset_util(i+1, ds)
                ds.pop()
        subset_util(0, [])
        return res