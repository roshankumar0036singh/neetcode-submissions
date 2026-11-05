# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root=TreeNode(preorder[0])
        queue=deque([root])
        in_i=0
        for val in preorder[1:]:
            node=TreeNode(val)
            parent=queue[-1]
            if parent.val!=inorder[in_i]:
                parent.left=node
            else:
                while queue and queue[-1].val == inorder[in_i]:
                    parent=queue.pop()
                    in_i+=1
                parent.right=node
            queue.append(node)
        return root
        
        