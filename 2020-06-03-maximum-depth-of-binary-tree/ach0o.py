# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self._max = 0
        def getDepth(depth, node):
            if node is None:
                self._max = max(self._max, depth)
                return
            getDepth(depth+1, node.left)
            getDepth(depth+1, node.right)
        getDepth(0, root)
        return self._max
