class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        2 appoaches:
            1. Can find if there are cycles in graph, if so then False
            2. while nodes with indegree 0, remove them and update new indegree,
                by end if nodes remain False, else True 
        """
        adj = collections.defaultdict(list)
        indegree = collections.defaultdict(set)
        q = deque()

        for tar, src in prerequisites:
            indegree[tar].add(src)
            adj[src].append(tar)


        for node in range(numCourses):
            if len(indegree[node]) == 0:
                q.append(node)
        
        count = 0
        while q:
            cur = q.popleft()
            count += 1

            for node in adj[cur]:
                indegree[node].discard(cur)
                if len(indegree[node]) == 0:
                    q.append(node)
        
        return count == numCourses

