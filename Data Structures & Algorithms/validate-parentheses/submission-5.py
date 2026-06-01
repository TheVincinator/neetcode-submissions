class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {"(" : ")", "{" : "}", "[" : "]"}
        for c in s:
            if c in m:
                stack.append(c)
            else:
                if not stack or c != m[stack[-1]]:
                    return False
                stack.pop()
        return len(stack) == 0