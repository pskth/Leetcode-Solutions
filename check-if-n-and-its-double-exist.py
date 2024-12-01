class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = set()

        for x in arr:
            if x / 2 in d or x * 2 in d:
                return True
            else:
                d.add(x)
        
        return False
