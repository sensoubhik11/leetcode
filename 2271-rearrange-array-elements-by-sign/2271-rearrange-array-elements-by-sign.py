class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        temp = [None]*len(nums)
        i_pos, i_neg = 0, 1
        for num in nums:
            if num > 0:
                temp[i_pos] = num
                i_pos += 2
            else:
                temp[i_neg] = num
                i_neg += 2
        
        return temp