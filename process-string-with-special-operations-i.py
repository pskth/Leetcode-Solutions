class Solution:
    def processStr(self, s: str) -> str:
        stack = []

        for c in s:
            if c.isalpha():
                stack.append(c)
            elif c == '*' and stack:
                stack.pop()
            elif c == '#':
                stack += stack
            else:
                stack = stack[::-1]
        
        return ''.join(stack)
