class Solution:
    def minimumLength(self, s: str) -> int:
        ans = 0
        count = collections.Counter(s)
        for v in count.values():
            if v >= 3:
                if v & 1:
                    ans += 1
                else:
                    ans += 2
            else:
                ans += v
        return ans
