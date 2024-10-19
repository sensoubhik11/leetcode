class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_arr = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum_arr.append(prefix_sum_arr[i-1] + nums[i])
            
        cnt = 0
        freq_map = {}
        for val in prefix_sum_arr:
            if val == k:
                cnt += 1
            if val-k in freq_map:
                cnt += freq_map[val-k]
            freq_map[val] = freq_map.get(val,0) + 1
        return cnt