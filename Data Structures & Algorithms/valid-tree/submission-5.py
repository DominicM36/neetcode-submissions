class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #tree means no cycle and no nodes unvisited
        #cycle through whole tree with dfs and check if any unvisited
        #first make adj list
        if len(edges) > n-1:
            return False
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)

        #loop through adj list with dfs
        #store prev node to track if seen to skip
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for neighbors in adj[node]:
                if neighbors == prev:
                    continue
                if not dfs(neighbors, node):
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n