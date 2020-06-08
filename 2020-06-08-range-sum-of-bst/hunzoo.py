class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.answer = 0

    def find_nodes(self, node, l, r):
        if node:
            if l <= node.val <= r:
                print(node.val)
                self.answer += node.val
            if node.val > l:
                self.find_nodes(node.left, l, r)
            if node.val < r:
                self.find_nodes(node.right, l, r)

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.find_nodes(root, L, R)
        return self.answer
