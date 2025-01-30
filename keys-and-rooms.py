class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        adj = {i:rooms[i] for i in range(n)}
        count = 0

        def dfs(at):
            nonlocal count
            if visited[at]:
                return
            else:
                count += 1
                visited[at] = True

                for x in adj[at]:
                    dfs(x)
        dfs(0)
        return count == n
