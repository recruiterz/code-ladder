import queue


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        q = queue.Queue()
        q.put((root, 0))
        
        result = []
        
        while not q.empty():
            i, level = q.get()
            
            if i is None:
                continue
            if i.val is None:
                continue
                
            try:
                if result[level] < i.val:
                    result[level] = i.val
            except:
                result.append(i.val)
                
            q.put((i.left, level + 1))
            q.put((i.right, level + 1))
                
        return result
