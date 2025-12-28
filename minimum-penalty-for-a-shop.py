class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        prefix_sum = [0] * (n + 1)

        for i, char in enumerate(customers):
            if char == 'Y':
                prefix_sum[i + 1] = prefix_sum[i] + 1
            else:
…            if total_penalty < min_penalty:
                best_hour = j
                min_penalty = total_penalty

        return best_hour
