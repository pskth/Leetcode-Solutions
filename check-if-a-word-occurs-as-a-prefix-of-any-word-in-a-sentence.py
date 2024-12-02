class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n = len(searchWord)
        sentence = sentence.split(' ')

        for i in range(len(sentence)):
            if len(sentence[i]) >= n and sentence[i][:n] == searchWord:
                return i + 1
        
        return -1
