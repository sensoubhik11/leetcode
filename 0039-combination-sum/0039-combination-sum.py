class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def comb_util(idx, target, ds):
            if target == 0:
                res.append(ds[:])
                return
            if idx == len(candidates):
                return
            
            if candidates[idx] <= target:
                ds.append(candidates[idx])
                comb_util(idx, target-candidates[idx], ds)
                ds.pop()
            comb_util(idx+1, target, ds)
        comb_util(0, target, [])
        return res