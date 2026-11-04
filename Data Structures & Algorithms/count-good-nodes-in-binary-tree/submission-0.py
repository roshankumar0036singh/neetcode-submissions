# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue=deque([(root,root.val)])
        count=0
        while queue:
            node,max_node=queue.popleft()
            if node.val>=max_node:
                count+=1
            max_node=max(node.val,max_node)
            if node.left:
                queue.append((node.left,max_node))
            if node.right:
                queue.append((node.right,max_node))
        return count

        