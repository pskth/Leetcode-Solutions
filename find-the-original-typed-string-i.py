class Solution:
    def possibleStringCount(self, word: str) -> int:
        consecutiveLetters = 0
        
        for i in range(1,len(word)):
            if word[i] == word[i-1]:
                consecutiveLetters += 1
        
        return consecutiveLetters + 1
                
            