import math


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = len(tasks)
        
        if n == 0:
            return l
        
        # 가장 많은 task 띄엄띄엄 배치 
        # task 사이에 n 개의 idle 배치
        
        
        # 빈칸에 다음 task 배치
        # idle 자리가 모자랄 경우, 남아있는 task + (task // n ) + 1 idle
        
        
        counter = dict()
        
        for t in tasks:
            
            count = counter.setdefault(t, 0)
            count += 1
            counter[t] = count
            
        largest_task_count = max(counter.values())
        
        
        # len(tasks) + 
        # max idle = n * (largest_task_count - 1)
        # same_largest_count
        
        same_largest_count = -1
        diff_count = 0
        
        for task, count in counter.items():
            if count == largest_task_count:
                same_largest_count += 1
                del counter[task]
                break
            else:
                diff_count += 1

        # if n * (largest_task_count - 1) < (l - largest_task_count):
            # return l

        # 18 + 12 - (18 - 4)
        # 30 + 12 - 14 + 
        
        # 12 + 5 - 6
        
        remainder = 0
        if diff_count >= n:
            remainder = (diff_count - largest_task_count)
            
        idle_time = n * (largest_task_count - 1)
        
        for count in counter.values():
            idle_time = idle_time - min(count, largest_task_count - 1)
            
        idle_time = min(0, idle_time)
        return l + idle_time
            
            
        
            
            
        
#         return l + n * (largest_task_count - 1) - (l - largest_task_count) + same_largest_count + remainder
        
        
