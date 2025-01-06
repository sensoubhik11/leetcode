class Solution:
    def myPow(self, x: float, n: int) -> float:
        # deals with non-negative powers
        def cal_pow(x, n):
            if n == 0:
                return 1
            a = cal_pow(x, n//2)
            if n%2 == 0:
                return a*a
            else:
                return x*a*a
        ans = cal_pow(x,abs(n))
        if n < 0:
            return 1/ans
        return ans