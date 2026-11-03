# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or root is p or root is q:
            return root
        
        left_subtree=self.lowestCommonAncestor(root.left,p,q)
        right_subtree=self.lowestCommonAncestor(root.right,p,q)
        
        if left_subtree and right_subtree:
            return root
        return left_subtree if left_subtree else right_subtree


            

        

        