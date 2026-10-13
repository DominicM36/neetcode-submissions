# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        #q tracks nodes on each level
        #add root
        #if node is non null add to level array
        #add children if they exist
        q.append(root)
        while q:
            qLen = len(q) #horizontal size of level
            level = [] #to store this level
            for i in range(qLen):
                node = q.popleft() #take node out of queue
                if node: #this check is important since it prevents q from populating with just null
                    level.append(node.val)
                    #add both children to q
                    #if child are null, will be skipped from adding to level
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

