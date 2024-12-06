class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1
        votes = 0
        for num in nums:
            if votes == 0:
                candidate = num
                votes += 1
            else:
                if num == candidate:
                    votes += 1
                else:
                    votes -= 1
        return candidate