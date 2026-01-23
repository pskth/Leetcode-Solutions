class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign, overflow = False, False
        num = 0 
        
        if not s:
            return num
        if s[0] in '+-':
            sign = True
…        
        if overflow:
            return -2**31 if sign and s[0] == '-' else 2**31 - 1
        
        if sign and s[0] == '-':
            return num * -1
        else:
            return num