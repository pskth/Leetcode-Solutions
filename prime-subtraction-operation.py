class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        def isPrime(n):
            for i in range(2,int(n ** (1/2)) + 1):
                if n % i == 0:
                    return False
            return True
        prev = 0
        
        for n in nums:
            maxPrime = 0
            uprBound = n - prev - 1
            
            while uprBound >= 2:
                if isPrime(uprBound):
                    maxPrime = uprBound
                    break
                uprBound -= 1

            if n - maxPrime <= prev:
                return False

            prev = n - maxPrime

        return True
