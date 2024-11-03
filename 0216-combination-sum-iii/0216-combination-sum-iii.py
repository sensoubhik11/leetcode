class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [x for x in range(1, 10)]
        res = []
        def comb_util3(idx, n, ds):
            if n == 0 and len(ds) == k:
                res.append(ds[:])
                return
            if len(ds) > k or idx == len(nums):
                return
            if(nums[idx] <= n):
                ds.append(nums[idx])
                comb_util3(idx+1, n-nums[idx], ds)
                ds.pop()
            comb_util3(idx+1, n, ds)
        comb_util3(0, n, [])
        return res