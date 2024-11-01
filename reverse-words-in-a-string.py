class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        print(arr)
        ans = ""
        for c in arr[::-1]:
            if c != '':
                ans += c + " "
        return ans[:-1]
