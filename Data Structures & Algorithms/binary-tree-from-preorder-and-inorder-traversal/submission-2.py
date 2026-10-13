# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #recursion
        #start at root, go through preorder list for following two children, set them to be the next two values
        #in order helps split array
        #need a check for when node reaches center of inorder list
        #can be done using pointers to both arrays, when center is reached, go back to node and build left side
        #recursive way to do it

        #too slow, need hashmap
        iomap = {val: i for i, val in enumerate(inorder)} 
        poi = 0
        def dfs(l,r):
            nonlocal poi
            if l > r:
                return None
            root_val = preorder[poi]
            poi += 1
            root = TreeNode(root_val)
            mid = iomap[root_val]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(inorder) - 1)






        # if not preorder or not inorder: #base case
        #     return None
        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0]) #find index of root in in order to find midway
        # #build left tree, will be all values to left of mid
        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # #build right tree, will be all values to the right of mid
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        # return root
        
