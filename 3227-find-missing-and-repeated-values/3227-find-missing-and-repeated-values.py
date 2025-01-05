class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        xor = 0
        k = len(grid)
        k *= k
        for i in range(1, k+1):
            xor = xor ^ i
        for row in grid:
            for num in row:
                xor = xor ^ num
        
        # xor = a^b
        mask = xor & (-xor)
        a,b = 0, 0
        for i in range(1, k+1):
            if mask & i:
                a ^= i
            else:
                b ^= i
        for row in grid:
            for num in row:
                if mask & num:
                    a ^= num
                else:
                    b ^= num
        for row in grid:
            for num in row:
                if num == a:
                    return [a, b]
                elif num == b:
                    return [b, a]
        return []
