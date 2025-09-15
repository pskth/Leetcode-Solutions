class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        b_set = set(brokenLetters)
        text = text.split(" ")
        count = 0
        
        for word in text:
            for char in word:
                if char in b_set:
                    break
            else:
                count += 1
        
        return count