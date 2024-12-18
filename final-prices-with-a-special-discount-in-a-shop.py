class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        '''
        Monotonic Stack Problem: Similar concept to infix to postfix stack operation (pop until
        prcedence of incoming element > precedence of top of stack)

        '''
        
        n = len(prices)
        stack = []
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]
            stack.append(i)

        return prices
