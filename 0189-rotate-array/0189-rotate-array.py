class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        k = n-k # turning right shift into left shift
        for i in range(math.gcd(k,n)):
            temp = nums[i]
            j = i
            while True:
                nxt_ptr = (j+k)%n
                if i == nxt_ptr:
                    nums[j] = temp
                    break
                nums[j] = nums[nxt_ptr]
                j = nxt_ptr

