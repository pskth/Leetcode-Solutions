class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        dfs starting from each node
            if not seen before
        
        check if cur node in local seen => cycle found
        check if in visited => no need to check again its clear
        """
        global_seen = set()
        local_seen = set()
        res = []
        adj = collections.defaultdict(list)
        
        for src, dst in prerequisites:
             adj[src].append(dst) 

        def dfs(i):
            if i in local_seen:
                return False
            if i in global_seen:
                return True

            local_seen.add(i)
            for nei in adj[i]:
                if dfs(nei) == False:
                    return False

            local_seen.remove(i)
            global_seen.add(i)
            res.append(i)

            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
        return res
        
