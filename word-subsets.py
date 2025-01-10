class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        subsetCount = {}
        for word in words2:
            temp = Counter(word)
            for letter in temp:
                if letter in subsetCount:
                    subsetCount[letter] = max(subsetCount[letter], temp[letter])
                else:
                    subsetCount[letter] = temp[letter]

        wordCount = {}
        ans = []
        for word in words1:
            wordCount[word] = Counter(word)

        for word in wordCount:
            for letter in subsetCount:
                if letter not in wordCount[word] or wordCount[word][letter] < subsetCount[letter]:
                    break
            else:
                ans.append(word)
        
        return ans
