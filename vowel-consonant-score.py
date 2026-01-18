class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vow, cons = 0, 0
        
        for c in s:
            if c in "aeiou":
                vow += 1
            elif c not in " 1234567890":
                cons += 1

        return 0 if cons <= 0 else floor(vow / cons)