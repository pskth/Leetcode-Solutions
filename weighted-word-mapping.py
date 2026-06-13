class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        """
        split in 2 parts:
        first find weight of each word
        convert weight to letter
        """
        res = []

        for word in words:
            wei = 0
            for letter in word:
                wei += weights[ord(letter) - ord('a')]
            
            val = wei % 26

            res.append(chr(ord('z') - val))

        return "".join(res)
