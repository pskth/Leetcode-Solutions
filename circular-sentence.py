class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words:list(int) = sentence.split(" ")
        fl = words[0][0]
        ll = words[-1][-1]
        if fl != ll:
            return False
        for word in words:
            ll = word[0]
            if fl != ll:
                return False
            fl = word[-1]
        return True
