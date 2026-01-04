class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum_divisors = 0

        for num in nums:
            div_count = 0
            div_sum = 0
            for div in range(1, int(math.sqrt(num))+1):
                if num % div == 0:
                    if div * div == num:
…                
            if div_count == 4:
                sum_divisors += div_sum
        
        return sum_divisors