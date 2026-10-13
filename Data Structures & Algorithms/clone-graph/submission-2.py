"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # #clone with bfs

        # #set for index of visited node
        # if not node:
        #     return None
        # #hashmap to map old values to new deep cloned values
        # oldToNew = {}
        # oldToNew[node] = Node(node.val)
        # q = deque([node])

        # while q:
        #     cur = q.popleft()
        #     for nei in cur.neighbors:
        #         if nei not in oldToNew:
        #             oldToNew[nei] = Node(nei.val)
        #             q.append(nei)
        #         oldToNew[cur].neighbors.append(oldToNew[nei])
        # return oldToNew[node]


        #dfs solution
        #hashmap mapping old nodes to new nodes
        newNodes = {}

        #cloning happens here
        def dfs(ognode):
            #base case
            if ognode in newNodes:
                #node already exists in
                return newNodes[ognode]

            if not ognode:
                return None

            #create the copynode
            copy = Node(ognode.val)
            #add copy node to list of new nodes
            newNodes[ognode] = copy

            #update neighbor for copynode
            for nei in ognode.neighbors:
                #copy's list gets appended with dfs of neighbor nodes
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)
             #clone neighbors
            #add to map
           
        