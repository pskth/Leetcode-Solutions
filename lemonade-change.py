class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = defaultdict(int)

        for bill in bills:
            print(bill, d)
            if bill == 20:
                if d[10] >= 1 and d[5] >= 1:
                    d[10] -= 1
                    d[5] -= 1
…                    return False
                d[10] += 1
            else:
                d[5] += 1
        
        return True