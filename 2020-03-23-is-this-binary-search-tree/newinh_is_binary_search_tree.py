""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
import queue

def check_binary_search_tree_(root):
    
    def is_bst(node, _min, _max):
        
        if node is None:
            return True
        
        if node.data <= _min or node.data >= _max:
            return False
        
        return is_bst(node.left, _min, node.data) and is_bst(node.right, node.data, _max)
    
    return is_bst(root, 0, 10000)

