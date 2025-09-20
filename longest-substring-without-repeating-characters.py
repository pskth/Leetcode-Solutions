class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            while l < r and s[r] in seen:
                seen.discard(s[l])
                l += 1

            seen.add(s[r])
            longest = max(longest, r - l + 1)
            

        return longest
            