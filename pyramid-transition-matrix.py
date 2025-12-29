class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        strong_base = {}
        
        for blocks in allowed:
            if blocks[:2] in strong_base:
                strong_base[blocks[:2]].add(blocks[2])
            else:
                strong_base[blocks[:2]] = set(blocks[2])\

…                return False
            else:
                memo[(top, base)] = False
                return False

        return bt("", bottom)