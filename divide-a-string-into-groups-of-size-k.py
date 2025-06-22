class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        numOfGroups = ceil(len(s) / k)
        groups = []
        j = 0

        for i in range(numOfGroups):
            groups.append(s[j:j+k])
            j += k
        
        groups[-1] += (k - len(groups[-1])) * fill

        return groups
