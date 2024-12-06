from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1
        for ch in t:
            freq[ch] -= 1
        for key in freq:
            if freq[key] != 0:
                return False
        return True