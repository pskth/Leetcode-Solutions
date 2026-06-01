class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        """
        we sort in desc order
        since free item can be smaller than equal to min price of every 2 items bought
        be greedy, buy 2 most costly items (they can never be free as per rules)
        3rd item --> free
        in similar fashion continue
        """
        cost.sort(reverse = True)

        cur = 0
        for i in range(2, len(cost), 3):
            cur += cost[i]
        
        return sum(cost) - cur
