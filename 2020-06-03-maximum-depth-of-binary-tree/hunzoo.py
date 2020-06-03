# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max = 0
        self.count = 1

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return self.max
        if not root.left and not root.right:
            if self.count >= self.max:
                self.max = self.count
        if root.left:
            self.count += 1
            self.maxDepth(root.left)
            self.count -= 1

        if root.right:
            self.count += 1
            self.maxDepth(root.right)
            self.count -= 1

        return self.max
