class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        adj = [[] for _ in range(n)]
        print(adj)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)

        visited = set()
        # def dfs(node,prev):
        #     if node in visited:
        #         return False
        #     visited.add(node)

        #     #need to check neighbors
        #     for nei in adj[node]:
        #         if nei == prev:
        #             continue
        #         if not dfs(nei, node):
        #             return False
        #     return True

        # return dfs(0,-1) and len(visited) == n
        q = deque([(0,-1)])
        #q.append([(0,-1)])
        visited.add(0)
        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                visited.add(nei)
                q.append((nei,node))
        return len(visited) == n
