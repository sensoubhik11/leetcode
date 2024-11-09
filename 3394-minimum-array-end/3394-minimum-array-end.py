class Solution:
    def minEnd(self, n: int, x: int) -> int:
        """
        We cannot tamper with the set bits in x since we will do AND opr of all numbers
        And we need to find numbers that are greater than it and not just that
        but also a fixed amount of those numbers.
        What we see is that we can set the unset bits in x and get larger numbers

        Say x = 5 = (101)b, n = 2 = (10)b
        At 1th posn of x, we can have either 0 or 1(2 ways).
        So x1 = x = 101, x2 = 111
        ans = 111

        say n = 3
        We now know that we need two zeroes(unset bits in x)
        x = 5 = 0101
        x2 = 0111
        x3 = 1101

        We see that basically the unset bit positions of original x follow the 
        simple count of n, i.e., 00, 01, 10
        The last (10)b = 3-1 = 2 is what we put in the unset positions of x
        to get the final number.
        More specifically we need to superimpose the bits of binary of n-1 on
        the unset bits of x
        """ 
        n_binary = bin(n-1)[2:]
        y = x
        shift = 0
        for bit in n_binary[::-1]:
            # finding unset posn
            while (1<<shift) & x:
                shift += 1
            y = y | int(bit) << shift # putting the bits of n-1 on unset posn of x one by one
            shift += 1
        return y