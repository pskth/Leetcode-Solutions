class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 1
        ans = s[0]
        prev = s[0]
        for c in range(1,len(s)):
            if prev == s[c]:
                count += 1
            else:
                count = 1
            prev = s[c]
            if count != 3: 
                ans += s[c]
            else:
                count -= 1
        return ans
