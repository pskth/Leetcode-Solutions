class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        clean_text = []

        for ch in s:
            if ch.isalnum():
                clean_text.append(ch.lower())

        return clean_text == clean_text[::-1]
