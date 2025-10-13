class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        cur = words[0]
        ans = [cur]
        curFreq = Counter(cur)

        for i in range(1, len(words)):
            if collections.Counter(words[i]) == curFreq:
                continue
            else:
                ans.append(words[i])
                cur = words[i]
                curFreq = Counter(cur)
    
        return ans
