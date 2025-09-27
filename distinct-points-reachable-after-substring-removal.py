class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        seen = set()
        cur = [0,0]
        l = 0
        val = {'U': 1, 'D': -1, 'L': -1, 'R': 1}
        for r in range(len(s)):
            if r < k:
                if s[r] in 'UD':
                    cur[0] += val[s[r]]
                else:
                    cur[1] += val[s[r]]
                continue

            seen.add(tuple(cur))
            if s[r] in 'UD':
                cur[0] += val[s[r]]
            else:
                cur[1] += val[s[r]]
            
            if s[l] in 'UD':
                cur[0] -= val[s[l]]
            else:
                cur[1] -= val[s[l]]

            l += 1

        seen.add(tuple(cur))
        return len(seen)
            
                