class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        q = list()
        q.append(("0000", 0))
        visited = {"0000"}
        
        des = set(deadends)
        
        while q:
            lock, count = q.pop(0)
            
            if lock == target:
                return count
            
            if lock in des:
                continue
                
            for d in range(4):
                u = self.rotate_up(lock, d)
                d = self.rotate_down(lock, d)
                
                if u not in visited:
                    q.append((u, count + 1))
                    visited.add(u)
                
                if d not in visited:
                    q.append((d, count + 1))
                    visited.add(d)
        return -1

    def rotate_up(self, lock: str, digit):
        l = list(lock)
        slot = l[digit]
        slot = (int(slot) + 1) % 10
        l[digit] = str(slot)
        return "".join(l)
    
    def rotate_down(self, lock: str, digit):
        l = list(lock)
        slot = l[digit]
        slot = (10 + int(slot) - 1) % 10
        l[digit] = str(slot)
        return "".join(l)

    
    # 8 * 7 * 6 * 5
