class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')':'(', '}':'{', ']':'['}
        for ch in s:
            # if we encounter closing bracket
            if ch in pair:
                if stack and stack[-1] == pair[ch]:
                    stack.pop()
                else:
                    return False
            # if we see opening bracket, push it onto stack
            else:
                stack.append(ch)
        # if stack empty, return True
        return not stack