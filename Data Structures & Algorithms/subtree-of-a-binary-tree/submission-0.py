# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #first thought, search through bst for subroot
        #edit just binary tree, have to check each level for it
        #can do iteratively checking value of subroot
        #get to node, from there check left and right
        #check if subroot is null, if so always true
        if not subRoot:
            return True
        #check root assuming subroot is treu
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    #helper function to validate tree
    def sameTree(self, root, subRoot) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return(self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        return False
        

        