class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2,3,5,7,11,13,17,19,23,29,31}
        res = 0
        for num in range(left, right + 1):
            one_count = bin(num).count('1')
            if one_count in primes:
                res += 1

        return res