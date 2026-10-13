# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #initial thought, brute force, traverse tree, store all of the tree in an array, return 
        #kth smallest from  array. Should be o(2n) time, o(n) memory
        #bst hints that there is a faster way to do it
        
        #use dfs and do an in order traversal till k elements have been seen to find k smallest
        arr = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        return arr[k-1]
        