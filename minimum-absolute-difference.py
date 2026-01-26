class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = math.inf
        res = []

        for i in range(1, len(arr)):
            if min_diff > abs(arr[i] - arr[i - 1]):
                res.clear()
                res.append([arr[i - 1], arr[i]])
                min_diff = abs(arr[i] - arr[i - 1])
            elif min_diff == abs(arr[i] - arr[i - 1]):
                res.append([arr[i - 1], arr[i]])
            
        return res