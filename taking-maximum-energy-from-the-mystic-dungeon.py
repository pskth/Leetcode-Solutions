class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        '''
        This solution is slower than other available dp solution.
        Check about stride and CPU Branch Prediction to know about this.
        '''
        prefixSum = []
        ans = -(math.inf)

        for i in reversed(range(len(energy))):
            ans = max(ans, energy[i])
            if i - k >= 0:
                energy[i - k] += energy[i]

        return ans