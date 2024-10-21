class Solution:
    def pow_util(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        a = self.pow_util(x, int(n/2))
        if n%2 == 0:
            return a*a
        else:
            return a*a*x

    def myPow(self, x: float, n: int) -> float:
        ans = self.pow_util(x, n)
        if n < 0:
            ans = 1/ans
        return ans