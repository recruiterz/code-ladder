# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.total = 0
        def get_sum(root):
            if not root:
                return 0
            if root.val < L:
                get_sum(root.right)
            elif root.val > R:
                get_sum(root.left)
            else:
                self.total += root.val
                get_sum(root.left)
                get_sum(root.right)
        get_sum(root)
        return self.total
