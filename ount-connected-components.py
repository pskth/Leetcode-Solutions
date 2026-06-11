class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = collections.defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(i, par):
            visited.add(i)

            for nei in adj[i]:
                if nei == par:
                    continue
                if nei not in visited:
                    dfs(nei, i)
        
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
            dfs(i, -1)
        
        return res
