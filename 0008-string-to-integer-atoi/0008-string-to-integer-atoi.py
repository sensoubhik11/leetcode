class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        is_neg = False
        is_leading_sign = True
        n = 0
        for i in range(len(s)):
            if i==0 and (s[i] == '+' or s[i] == '-'):
                if s[i] == '-':
                    is_neg = True
            elif s[i].isdigit():
                n = 10*n + int(s[i])
            else:
                break
        if is_neg:
            n = -n
        if n < -2**31:
            n = -2**31
        elif n > 2**31-1:
            n = 2**31 -1
        return n