class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ans = ""
        date = date.split("-")
        for s in date:
            ans += bin(int(s))[2:]
            ans += '-'
        return ans[:-1]
