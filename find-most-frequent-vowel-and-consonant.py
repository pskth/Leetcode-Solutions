class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = collections.defaultdict(int)
        maxVowel = maxConsonant = 0
        
        for let in s:
            freq[let] += 1
            if let in "aeiou":
                maxVowel = max(maxVowel, freq[let])
            else:
                maxConsonant = max(maxConsonant, freq[let])

        return maxVowel + maxConsonant