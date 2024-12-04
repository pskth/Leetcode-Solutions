class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        ptr = 0

        def checkNextChr(curChar, c):
            nextchr = chr(ord(curChar) + 1)
            if curChar =='z':
                nextchr = 'a'
            return nextchr == c
    
        for c in str2:
            while ptr < len(str1):
                if str1[ptr] == c:
                    ptr += 1
                    break
                elif checkNextChr(str1[ptr], c):
                    ptr += 1
                    break
                else:
                    ptr += 1
            else:
                return False
        
        return True
