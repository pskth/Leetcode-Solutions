class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        curScore = 0
        left = 0
        right = s.count('1')

        for i in range(len(s) - 1):
            if s[i] == '1':
                right -= 1
            else:
                left += 1
            curScore = left + right
            score = max(score, curScore)
        
        return score
