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
        '''
        class Solution:
            def isCircularSentence(self, sentence: str) -> bool:
                words:list(int) = sentence.split(" ")
                #Intially we use fl to compare first letter of first word with last letter of the last word. Since in the first iteration we don't have to do any other comparisions, we use fl to store the last letter of the last word.
                fl = words[-1][-1]
                ll = words[-1][-1]
                for word in words:
                    ll = word[0]
                    if fl != ll:
                        return False
                    fl = word[-1]
                return True
        '''
