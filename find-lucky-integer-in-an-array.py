class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luckyInt = -1
        freq = collections.Counter(arr)

        for key in freq:
            if key > luckyInt and key == freq[key]:
                luckyInt = key

        return luckyInt 