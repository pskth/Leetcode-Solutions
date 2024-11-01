class Solution:
    def reverseVowels(self, s: str) -> str:
        pos = []
        ans = ""
        for c in range(len(s)):
            if s[c] in 'aeiouAEIOU':
                pos.append(c)
        i = -1
        for c in range(len(s)):
            if s[c] in "aeiouAIEOU":
                ans += s[pos[i]]
                i -= 1
            else:
                ans += s[c]  

        return ans
