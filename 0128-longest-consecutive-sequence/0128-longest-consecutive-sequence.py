class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1
        max_cnt = 0
        for num in nums:
            if num+1 not in freq_map:
                cnt = 0
                while num in freq_map:
                    cnt += 1
                    num -= 1
                max_cnt = max(max_cnt, cnt)
        return max_cnt