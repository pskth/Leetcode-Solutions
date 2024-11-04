class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c = Counter(deck)
        x = c.values()
        if reduce(gcd,x) > 1:
            return True
        else:
            return False
