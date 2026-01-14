class Solution:
    def trailingZeroes(self, n: int) -> int:
        no_of_fives = 0
        k = 5

        while k <= n:
            no_of_fives += (n // k)
            k *= 5 
        
        return no_of_fives