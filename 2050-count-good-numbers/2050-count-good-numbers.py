class Solution:
    def myPow(self, x, n):
        MOD = int(1e9+7)
        if n == 0:
            return 1
        a = self.myPow(x, n//2)
        a = a%MOD
        if n%2 == 0:
            return (a*a)%MOD
        else:
            return (a*a*x)%MOD

    def countGoodNumbers(self, n: int) -> int:
        MOD = int(1e9+7)
        pow_of_5 = 0
        pow_of_4 = 0
        if n%2 == 0:
            pow_of_5 = n//2
            pow_of_4 = n//2
        else:
            pow_of_5 = n//2 + 1
            pow_of_4 = n - pow_of_5
        #permutations at even indices
        p0 = self.myPow(5, pow_of_5)
        # permutations at odd indices
        p1 = self.myPow(4, pow_of_4)

        return (p0*p1)%MOD
