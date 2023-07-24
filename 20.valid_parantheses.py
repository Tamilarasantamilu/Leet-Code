class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if len(stack) > 0 and i in d and stack[-1] == d[i]:
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0