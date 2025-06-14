class Solution:
    def average(self, salary: List[int]) -> float:
        sumSal = 0
        minSal = inf
        maxSal = -inf
        for s in salary:
            if minSal > s:
                minSal = s
            if maxSal < s:
                maxSal = s
            sumSal += s
        return (sumSal - minSal - maxSal) / (len(salary) - 2) 