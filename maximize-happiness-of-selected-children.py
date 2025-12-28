class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res, diff = 0, 0

        for child in happiness[:k]:
            if child - diff <= 0:
                break
            res += child - diff
            diff += 1

        return res