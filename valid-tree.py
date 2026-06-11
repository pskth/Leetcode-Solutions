class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = collections.defaultdict(list)

        if len(edges) != n - 1:
            return False

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(i, par):
            if i in visited:
                return False
            
            visited.add(i)

            for nei in adj[i]:
                if nei == par:
                    continue
                if dfs(nei, i) == False:
                    return False
            
            return True
            
        return dfs(0, -1) and len(visited) == n
