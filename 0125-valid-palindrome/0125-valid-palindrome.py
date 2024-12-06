class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s)-1
        while low < high:
            if not s[low].isalnum():
                low += 1
            elif not s[high].isalnum():
                high -= 1
            elif s[low].lower() != s[high].lower():
                return False
            else:
                low += 1
                high -= 1
        return True
            