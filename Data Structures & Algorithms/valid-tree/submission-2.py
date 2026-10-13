class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #tree means no cycle and no nodes unvisited
        #can do dfs on the tree and count the visited against the edges + 1
        if not n:
            return True
        if len(edges) > (n - 1):
            return False
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        
        def dfs(node, prev):
            #already visited, detected loop
            if node in visit:
                return False
            visit.add(node)
            for j in adj[node]:
                if j == prev:
                    #skip
                    continue
                if not dfs(j, node):
                    return False
            return True
        #return dfs with previous being random node, then starting at root
        #if n == numbers of nodes visited, detected they are all connected
        return dfs(0,-1) and n == len(visit)