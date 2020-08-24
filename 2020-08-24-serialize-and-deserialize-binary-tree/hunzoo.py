# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        
        l = 0
        def depth_ck(node, level):
            if node:
                nonlocal l
                level += 1
                l = max(l, level)
                depth_ck(node.left, level)
                depth_ck(node.right, level)
                
        depth_ck(root, 0)        
        
        ans = '['
        queue = [(root, 1)]
        
        while queue:
            cur_node, level = queue.pop(0)
            if level <= l:
                if cur_node:
                    ans += str(cur_node.val)
                    ans += ','
                    queue.append((cur_node.left, level + 1))
                    queue.append((cur_node.right, level + 1))
                else:
                    ans += 'null'
                    ans += ','
        return ans[:-1] + ']'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        l = data[1:-1].split(',')
        tree = [TreeNode(l[0])]
        for i in range(len(l)):
            parent = tree[i]
            left_idx = (i * 2) + 1
            if left_idx <= len(l) - 1:
                left_node = TreeNode(l[left_idx])
                parent.left = left_node
                tree.append(left_node)
            right_idx = (i * 2) + 2
            if right_idx <= len(l) - 1:
                right_node = TreeNode(l[right_idx])
                parent.right = right_node
                tree.append(right_node)
        return tree[0]

    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
