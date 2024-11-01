class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        minLen = min(len(word1),len(word2))

        for i in range(minLen):
            ans += word1[i]
            ans += word2[i]
        if len(word1) == minLen:
            ans += word2[minLen::]
        else:
            ans += word1[minLen::]
        return ans
