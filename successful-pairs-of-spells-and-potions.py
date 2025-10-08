class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []

        def binSearch(key):
            l = 0
            r = len(potions) - 1
            sol = len(potions)

            while l <= r:
                mid = (l + r) // 2
                if potions[mid] >= key:
                    sol = mid
                    r = mid - 1
                else:
                    l = mid + 1

            return sol

        for spell in spells:
            key = int(ceil(success / spell))
            index = binSearch(key)
            ans.append(len(potions) - index)

        return ans