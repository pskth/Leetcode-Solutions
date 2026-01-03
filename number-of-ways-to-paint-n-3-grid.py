class Solution:
    def numOfWays(self, n: int) -> int:
        if n == 1:
            return 12

        MOD = 10**9 + 7
        abc_way = 6
        aba_way = 6

        for i in range(n - 1):
            new_abc_way = (2 * abc_way + 2 * aba_way) % MOD
            new_aba_way = (2 * abc_way+ 3 * aba_way) % MOD

            abc_way = new_abc_way
            aba_way = new_aba_way 
        
        return (abc_way + aba_way) % MOD