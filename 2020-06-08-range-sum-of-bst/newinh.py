# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        if root is None:
            return 0

        l = self.rangeSumBST(root.left, L, R) if root.val > L else 0
        r = self.rangeSumBST(root.right, L, R) if root.val < R else 0
        
        v = root.val if L <= root.val <= R else 0 
        return l + r + v
