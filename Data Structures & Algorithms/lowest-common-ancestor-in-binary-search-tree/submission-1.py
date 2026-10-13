# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #need to find split
        #if p and q are both greater or less than root need to continue moving down. Recursion base case happens
        #when there is a split, return that node


        # if not root or not p or not q:
        #     return None
        # if root == p or root == q:
        #     return root
        # if (root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val):
        #     return root
        # if root.val < p.val and root.val < q.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # #if root > p and root > q:
        # else:
        #     return self.lowestCommonAncestor(root.left, p, q)

        #try iterative to find split

        cur = root
        while cur:
            #go down right side
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur


    
        