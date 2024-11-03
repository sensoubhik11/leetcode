class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def comb_util2(idx, target, ds):
            if target == 0:
                res.append(ds[:])
                return
            
            for i in range(idx, len(candidates)):
                if i>idx and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                comb_util2(i+1, target-candidates[i], ds)
                ds.pop()
        
        comb_util2(0, target, [])
        return res
        