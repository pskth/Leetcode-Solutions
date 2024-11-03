class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            temp = s[1:]
            temp += s[0]
            if temp == goal:
                return True
            s = temp
        return False
