class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        prefixSum = []
        ans = -(math.inf)

        for i in reversed(range(len(energy))):
            ans = max(ans, energy[i])
            if i - k >= 0:
                energy[i - k] += energy[i]

        return ans