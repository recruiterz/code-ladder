# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        max_depth = 0
        stack = list()
        
        stack.append((1, root))
        
        while stack:
            depth, node = stack.pop()
            if not node:
                continue
            
            if max_depth < depth:
                max_depth = depth
                
            stack.append((depth + 1, node.left))
            stack.append((depth + 1, node.right))
        return max_depth
