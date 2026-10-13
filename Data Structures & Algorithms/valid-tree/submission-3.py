class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #tree means no cycle and no nodes unvisited
        #can do dfs on the tree and count the visited against the edges + 1
        if not n:
            return True

        #make adj list
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)

        visited = set()

        def dfs(n, prev):
            if n in visited:
                return False
            visited.add(n)
            #cycle through all the edges of each node
            for neighbor in adj[n]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, n):
                    return False
            return True

                

        return dfs(0, -1) and len(visited) == n