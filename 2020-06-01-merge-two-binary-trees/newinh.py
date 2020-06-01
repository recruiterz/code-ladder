# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        stack = []
        
        if t1:
            one, another = t1, t2
        else:
            one, another = t2, t1
            
        stack.append((None, one, another, None))
        
        while stack:
            
            l, n1, n2, r = stack.pop()
            
            if n1 is None and n2 is None:
                continue
            
            n1 = n1 or TreeNode()
            n2 = n2 or TreeNode()
            
            n1.val += n2.val
            
            if l:
                l.left = n1
            if r:
                r.right = n1
            
            stack.append((n1, n1.left, n2.left, None))
            stack.append((None, n1.right, n2.right, n1))
        
        return one
        
