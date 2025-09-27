class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        count = Counter(s)
        c = defaultdict(str)
        ans = ''
        cur = 0
        curv = 0
        
        for key, val in count.items():
            c[val] += key

        for val, key in c.items():
            if len(key) > cur:
                cur = len(key)
                ans = key
                curv = val
            if len(key) == cur:
                if val > curv:
                    curv = val
                    cur = len(key)
                    ans = key
                
        return ans